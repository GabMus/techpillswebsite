from django.db import models

# Create your models here.

# title, description, thumb, date, time, url
class Video(models.Model):
    #  id is already defined as default in django
    vid_id = models.TextField(blank=False)
    title = models.TextField(blank = False)
    description = models.TextField(blank = False)
    thumb =  models.TextField(blank = False)
    date_time = models.DateTimeField(auto_now_add = False)
    url = models.TextField(blank = False)

    def __str__(self):
        return self.title

class Gear(models.Model):
    name = models.TextField(blank=False)
    description = models.TextField(blank=False)
    pic = models.TextField(blank=True)
