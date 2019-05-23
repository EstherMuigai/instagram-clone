from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/')
    bio = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    pic = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(blank=True,max_length = 255)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.profile.user.username}'

class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.username}'

class Comment(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'

