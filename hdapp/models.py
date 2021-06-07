from re import T
from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import AbstractUser,User
from django.db.models.fields import IntegerField, TextField, related
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Neighbourhood(models.Model):
    hdname = models.CharField(max_length = 40)
    location = models.CharField(max_length=30)
    occupants = models.IntegerField(default=80)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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
    username = models.CharField(max_length=40,blank = True, null = True,)
    email = models.EmailField(_('email address'), unique = True)
    native_name = models.CharField( max_length=100)
    role = models.CharField(max_length=40, choices=ROLE_TYPE_CHOICES, default=USER)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
      return "{}".format(self.email)

    def save_superuserdmin(self):
        self.save()
    def save_admin(self):
        self.save()
    def save_user(self):
        self.save()


class Profile(models.Model):
    about = models.TextField(max_length=68)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    my_location = models.CharField(max_length=40)
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
    content = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    when_posted = models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        self.save()

class Business(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()

class Department(models.Model):
    contact = models.IntegerField()
    name = models.CharField(max_length=40, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


    def save_department(self):
        self.save()
