from django.contrib import admin

# Register your models here.

from authenticate.models import fileupload
admin.site.register(fileupload)