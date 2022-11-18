from django.db import models

# Create your models here.
class Categorys(models.Model):
    name=models.CharField(max_length=100, null=False, blank =False)

    def  __str__(self):
        return self.name

class Videos(models.Model):
    Category=models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True, blank=True)
    video=models.FileField(upload_to='videos/video_files' )
    description=models.TextField(max_length=500, null=False, blank =False)

    def  __str__(self):
        return self.description       