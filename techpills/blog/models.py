from django.db import models

# Create your models here.

class Article(models.Model):
    #  id is already defined as default in django
    title = models.TextField(blank = False)
    content = models.TextField(blank = False)
    pic =  models.TextField(blank = True)
    date_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
