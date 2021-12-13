from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class fileupload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='Doc/')
    created_at = models.DateTimeField(default=timezone.now)

