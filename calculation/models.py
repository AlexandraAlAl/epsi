from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey('extuser.ExtUser')
    title = models.CharField(max_length=25)
    url = 'calculation/'
    file = models.FileField(upload_to=url, blank=True)
    file_name = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    csi = models.IntegerField(default=0)
    loyalty = models.IntegerField(default=0)
    regress = models.IntegerField(default=0)
    one = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    four = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


