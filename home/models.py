from django.db import models

# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8578ba79749dccf97940e6e91a4361f36a38d2e4

class User(models.Model):
    """ユーザー"""
    name = models.CharField(max_length=256)
    comment = models.TextField()
    icon = models.ForeignKey(Category,on_delete=models.CASCADE)


class Category(models.Model):
    """カテゴリー
    Galary(CG,イラスト,サービス)
    News,Blog"""
    name = models.CharField(max_length=256)

class Works(models.Model):
    """作品のモデル"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ForeignKey(Works_image,on_delete=models.CASCADE)
    user = models.ForeignKey(User)

class News(models.Model):
    """アクティビティ"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ForeignKey(News_image,on_delete=models.CASCADE)
    user = models.ForeignKey(User)

class Idea(models.model):
    """アイディア"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    good = models.IntegerRangeField(min_value=0, max_value=100)
    user = models.ForeignKey(User)

class progress(models.model):
    """進捗"""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User)


class Icon(models.Model):
    Icon = models.ImageField(upload_to='images/')

class News_image(models.Model):
    news_image = models.ImageField(upload_to='images/')

class Works_image(models.Model):
    works_image = models.ImageField(upload_to='images/')
