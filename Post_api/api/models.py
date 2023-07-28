from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
   



