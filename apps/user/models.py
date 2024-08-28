from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.base.models import BaseModel


class User(AbstractUser, BaseModel):
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    phone_number = models.CharField(max_length=225, null=True, blank=True, unique=True)

    def __str__(self):
        return self.username


class Client(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="clients/", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    job = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name
