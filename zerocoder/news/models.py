from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Заголовок новости', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации')