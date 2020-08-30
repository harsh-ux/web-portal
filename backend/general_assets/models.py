from django.db import models
from django.contrib.auth.models import User


class Competetion(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 300)
    img_tile = models.ImageField(default='default.jpg', upload_to='project_pics')
    positions = (("1", "First"),
                 ("2","Second"),
                 ("3","Third"),
                 ("Paticipated","Not among the top three"))
    result = models.CharField(max_length = 30, choices = positions)
    participants = models.ManyToManyField(User)
    def __str__(self):
        return str(self.name)


class HomeCarousel(models.Model):
    title = models.CharField(max_length =20, blank=True, default='')
    description = models.TextField(max_length= 300, blank=True, default='')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    img_tile = models.ImageField(default='default.jpg', upload_to='home_carousel_pics')
    url = models.URLField(max_length=200, null=True, blank=True)
    url_name = models.CharField(max_length=20, null=True, blank=True)


class News(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    url = models.URLField(max_length=200, null=True, blank=True)
    url_name = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    description = models.TextField(max_length=300)
    img_tile = models.ImageField(default='default.jpg', upload_to='news_pics')
    is_latest = models.BooleanField(default=True)


class UpEvents(models.Model):
    title = models.CharField(max_length =50, blank=True, default='')
    url = models.URLField(max_length=200, null=True, blank=True)
    url_name = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    description = models.TextField(max_length=300)
    img_tile = models.ImageField(default='default.jpg', upload_to='up_events_pics')
