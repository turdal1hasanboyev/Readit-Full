from django.db import models

from ckeditor.fields import RichTextField

from apps.base.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, null=True, blank=True, unique=True)
    subject = models.CharField(max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name
