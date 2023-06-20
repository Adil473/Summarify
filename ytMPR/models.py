from django.db import models

# Create your models here.

from embed_video.fields import EmbedVideoField

class Display_Video(models.Model):
    video = EmbedVideoField()  # same like models.URLField()