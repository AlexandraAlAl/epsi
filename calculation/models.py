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
    delete_date = models.DateTimeField()
    csi = models.FloatField(default=0)
    loyalty = models.FloatField(default=0)
    regress = models.FloatField(default=0)
    one = models.FloatField(default=0)
    two = models.FloatField(default=0)
    three = models.FloatField(default=0)
    four = models.FloatField(default=0)
    five = models.FloatField(default=0)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


