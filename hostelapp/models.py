# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Employee(AbstractUser):

    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.EmailField(unique=True)
    phone = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100)
    approved_status = models.IntegerField(default=0)
    adhar_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    

    # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(Group, related_name='employee_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='employee_user_permissions')

    def __str__(self):
        return self.email


class LeaveApply(models.Model):
    USERNAME_FIELD = 'apply_by'  
    apply_by = models.CharField(max_length=100)
    fromdate = models.CharField(max_length=30)
    todate = models.CharField(max_length=30)
    reason = models.CharField(max_length=30)
    approved_status = models.IntegerField(default=0)
    approved_status_parents = models.IntegerField(default=0)


class Complaints(models.Model):
    USERNAME_FIELD = 'apply_by'  
    apply_by = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=True, null=True)
    complaint_type = models.CharField(max_length=100)
    sub_complaint_type = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    note = models.CharField(max_length=1000)
    complaint_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    resolve_status = models.IntegerField(default=0)    

    
class Notice(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    date = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=100000)


class Document(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    document_name = models.CharField(max_length=100)
    Document_image = models.FileField(upload_to='profile_images/', blank=True, null=True)  


class News_letter(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    date = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=100000)

class Phone_Directory(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=True, null=True)
    position = models.CharField(max_length=100)
    phone = models.TextField(max_length=100000)
    email = models.EmailField(unique=True) 
    photo = models.ImageField(upload_to='profile_images/', blank=True, null=True) 


class Facility_Request(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    date = models.CharField(max_length=100,blank=True, null=True)
    facility = models.CharField(max_length=100)
    desc = models.TextField(max_length=100000)
    approved_status = models.IntegerField(default=0)
    

class Scorecard(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    semister = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    scorecard_image = models.FileField(upload_to='profile_images/', blank=True, null=True) 

class Refund_Request(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    approved_status = models.IntegerField(default=0)
   
