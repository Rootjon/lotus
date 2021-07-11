from django.db import models
from django.urls import reverse

# Create your models here.

class Slider (models.Model):
    headline = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='slider_images/')
    short_decription = models.TextField()


    def __str__(self) :
        return self.headline


class Feature (models.Model):
    headline = models.CharField(max_length=150)
    slug =models.SlugField()
    thumnail =models.ImageField(upload_to ='carousel/images/')
    short_description = models.TextField()
    description=models.TextField()
    creation=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.headline


    def get_absolute_url(self):
        return reverse("blog:blog_details", kwargs={"slug": self.slug})
    

