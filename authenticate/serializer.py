from authenticate.models import fileupload
from rest_framework import serializers

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = fileupload
        fields = "__all__"