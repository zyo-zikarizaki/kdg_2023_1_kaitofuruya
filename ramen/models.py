from django.db import models
from .consts import MAX_RATE

RATE_CHOICES={(x,str(x))for x in range(0,MAX_RATE + 1)}
CATEGORY=(('ニュース','ニュース'),('特集','特集'))


class Ramen(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    staff = models.TextField()
    story = models.TextField()
    music = models.CharField(max_length=100)
    acter = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=100)
    ramen=models.ForeignKey(Ramen, on_delete=models.CASCADE)
    rate=models.IntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.title
    
class Future(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    staff = models.TextField()
    story = models.TextField()
    music = models.CharField(max_length=100)
    acter = models.TextField()
    thumbnail_future = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    story = models.TextField()
    thumbnail_news = models.ImageField(null=True, blank=True)
    category=models.CharField(max_length=100,choices=CATEGORY)

    def __str__(self):
        return self.title
    
class Legend(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    staff = models.TextField()
    story = models.TextField()
    music = models.CharField(max_length=100)
    acter = models.TextField()
    thumbnail_legend = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title