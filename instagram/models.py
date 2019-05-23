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

    def __str__(self):
        return f'{self.profile.user.username}'

class Following(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField('status', default=False)

    def __str__(self):
        return f'{self.following.user.username}'


