from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  def __str__(self):
    return self.username

class AllBlog(models.Model):
  owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=40)
  description=models.TextField()
  image=models.ImageField(upload_to="images/")

  
