from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField('Название', max_length=256)
    content = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    cover = models.ImageField('Обложка', upload_to='post/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def get_absolute_url(self):
        return reverse('post:detail', args=[self.pk])
