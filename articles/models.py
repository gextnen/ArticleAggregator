from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.TextField(
        verbose_name='Заголовок',
    )
    content = models.TextField(
        verbose_name='Текст',
    )
    url = models.URLField(
        verbose_name='Ссылка',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
