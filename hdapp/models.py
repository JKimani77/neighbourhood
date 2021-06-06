from re import T
from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import AbstractUser,User
from django.db.models.fields import IntegerField, TextField

class Neighbourhood(models.Model):
    hdname = models.CharField(max_length = 40)
    location = models.CharField(max_length=30)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_neighbourhood(self):
        self.save()
    def del_neighbourhood(self):
        self.delete()
    def update_occupants(self,occupants ):
        self.update

    @classmethod
    def get_neighbourhood_id(cls, id):
        hood = Neighbourhood.objects.get(pk=id)
        return hood

#
class User(AbstractUser):
    
    SUPERUSER_ADMIN = 'SUPERUSER ADMIN'
    ADMIN = 'ADMIN'
    USER = 'USER'
    ROLE_TYPE_CHOICES = [
        (SUPERUSER_ADMIN, 'SUPERUSER ADMIN'),
        (ADMIN, 'ADMIN'),
        (USER, 'USER')
    ]
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_TYPE_CHOICES, default=USER)
    
    def save_superuserdmin(self):
        self.save()
    def save_admin(self):
        self.save()
    def save_user(self):
        self.save()


class Profile(models.Model):
    about = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    my_location = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def save_pfile(self):
        self.save()
    def delete_pfile(self):
        self.delete()
    
    @classmethod
    def get_pfile_id(cls, id):
        profile = cls.objects.get(pk=id)
        return profile
    def update_bio(self, about):
        self.about = about
        self.save()


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    when_posted = models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        self.save()

class Business(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()

class Department(models.Model):
    contact = models.IntegerField()
    name = models.CharField(max_length=30, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


    def save_department(self):
        self.save()
