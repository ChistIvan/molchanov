from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField('Наименование', max_length=200, db_index=True)
    slug = models.SlugField('Слаг', max_length=150, unique=True)
    body = models.TextField('Текст', blank=True, db_index=True)
    date_pub = models.DateTimeField('Время публикации', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.title}'