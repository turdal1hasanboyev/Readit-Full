from django.db import models

import uuid

from django.urls import reverse
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

from apps.base.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=225, null=True, blank=True, unique=True, db_index=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Category(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=225, null=True, blank=True, unique=True, db_index=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Article(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=225, null=True, blank=True, unique=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="article_photos/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)
    web_site = models.URLField(unique=True, null=True, blank=True, max_length=225)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=225)

    def __str__(self):
        return self.name
