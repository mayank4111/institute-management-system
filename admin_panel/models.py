from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='admin_profiles/',blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Admin"

class Announcements(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class StaffMembers(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField(help_text='Years of experience')
    email = models.EmailField()
    phone= models.CharField(max_length=15)
    photo = models.ImageField(upload_to='staff/',blank=True, null=True)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

