from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey('extuser.ExtUser')
    title = models.CharField(max_length=200)
    file=models.FileField(upload_to='calculation')
    created_date = models.DateTimeField(default=timezone.now)
    csi = models.IntegerField(default=0)
    loyalty = models.IntegerField(default=0)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


