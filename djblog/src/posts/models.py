from django.db import models
'''
title
content
image
author

'''
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'post_user')
    title = models.CharField( max_length=100)
    content = models.TextField(max_length=5000,verbose_name = 'Content')
    active = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'posts/')
    
    def __str__ (self):
        return self.title    