from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    images = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

