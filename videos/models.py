from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


# Create your models here.
class Categorys(models.Model):
    name=models.CharField(max_length=100, null=False, blank =False)

    def  __str__(self):
        return self.name

class Videos(models.Model):
    Category=models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True, blank=True)
    video=models.FileField(upload_to='videos/video_files',validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv'] )] )
    description=models.TextField(max_length=500, null=False, blank =False)
    # created_time=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.description       