from django.db import models
from django.contrib.auth.models import User

class ImageGallery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=255)
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    description = models.TextField()


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('beta_player', 'Beta Player'),
        ('company_user', 'Company User'),
        ('subscriber', 'Subscriber'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
