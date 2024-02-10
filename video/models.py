from django.db import models
from posts.models import *
# Create your models here.
class VIdeo(models.Model):
    title = models.CharField(max_length=155)
    context = models.TextField(blank=True)
    create_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)
    vidoe= models.FileField(upload_to='videos/')
    is_publish =models.BooleanField(default=True)
    category = models.ForeignKey("Category" ,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'

class Category(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категории'