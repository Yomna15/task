from django.db import models

# Create your models here.

class video(models.Model):
    video = models.FileField(upload_to="files/")

    def __str__(self):
        return self.video.url