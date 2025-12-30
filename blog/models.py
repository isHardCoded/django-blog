from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
    
    def __str__(self):
        return self.name

class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)
   
    def with_author_and_tags(self):
        return self.select_related('author').prefetch_related('tags')
   
    def recent_first(self):
        return self.order_by('-created_at')

class Article(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='Автор')
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True, verbose_name='Теги')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
   
    objects = ArticleQuerySet.as_manager()
   
    def __str__(self):
        return self.title
   
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        