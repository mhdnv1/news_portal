from django.db import models
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=155)
    context = models.TextField(blank=True)
    create_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)
    photo= models.ImageField(upload_to='photo' , blank=True)
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