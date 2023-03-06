from django.db import models
from custom_auth.models import CustomUser


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=10000, verbose_name='Текст')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    likes = models.PositiveIntegerField(default=0, verbose_name='Лайки')

    def __str__(self):
        return self.title + ' by ' + self.author.username

    def total_comments(self):
        return self.comments.all().count()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-id']
