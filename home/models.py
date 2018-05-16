from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """カテゴリー
    Galary(CG,イラスト,サービス)
    News,Blog"""
    name = models.CharField(max_length=256)

class Gallery(models.Model):
    """作品のモデル"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class News(models.Model):
    """アクティビティ"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')