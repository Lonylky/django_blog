from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse



# Create your models here.


# core_category
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return self.title

    class Meta:
        ordering =['title']
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='articles/', blank=True, null=True)
    views = models.PositiveSmallIntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'article_id': self.pk})

    def img_preview(self):
        if not self.image:
            return''
        return mark_safe(f'<img src="{self.image.url}" width="100" height="100">')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Comment')

    def __str__(self):
        return f'{self.author}: {self.article}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)


class DisLike(models.Model):
    user = models.ManyToManyField(User, related_name='dislikes')
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='dislikes', null=True, blank=True)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='dislikes', null=True, blank=True)












