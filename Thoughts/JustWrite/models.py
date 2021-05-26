from django.db import models
from django.contrib.auth.models import User

class add_blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    heading = models.CharField(max_length=100, default="")
    body = models.TextField()

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images', null= True, blank= True)
    address= models.TextField(default="")
    mobile_no = models.CharField(max_length=10, default ="")
    about= models.TextField(default="")
    dob= models.DateField(null= True, blank= True)
    


# Create your models here.
