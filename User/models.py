from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=500, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    
    def __str__(self):
        return self.user.username
    
class UserBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.CharField(max_length=200, null=True)
    
    
    def __str__(self):
        return f"blog id {str(self.id)} by {self.user.username}"