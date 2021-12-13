from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from authenticate.models import fileupload
from authenticate.serializer import FileUploadSerializer
from django.http import HttpResponse

class FileUploadView(APIView):

    def post(self,request):
        data = request.data
        res_status,output_detail = status.HTTP_400_BAD_REQUEST,"Failed"
        serializer = FileUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res_status,output_detail = status.HTTP_200_OK,"Success"
        else:
            output_detail = serializer.errors
        context = {
            "detail":output_detail
        }
        return Response (context, status=res_status, content_type="application/json")
    
    def get(self,request):
        req_data = request.GET
        current_site = request.get_host()
        scheme = request.scheme + "://"
        res_status,output_detail = status.HTTP_400_BAD_REQUEST,"Failed"
        data = []
        if req_data.get('id',False):
            id = req_data['id']
            file_obj = fileupload.objects.get(id=id)
            data =scheme + current_site + file_obj.file.url
            res_status,output_detail = status.HTTP_200_OK,"Success"
            context = {
                "detail":output_detail,
                'data':data
            }
        else:
            file_obj = fileupload.objects.all().order_by('-created_at')
            serializer = FileUploadSerializer(file_obj,many=True)
            data = serializer.data
            res_status,output_detail = status.HTTP_200_OK,"Success"
            context = {
                "detail":output_detail,
                'data':data
            }
        return Response (context, status=res_status, content_type="application/json")



