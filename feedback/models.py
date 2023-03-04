from django.db import models

from custom_auth.models import CustomUser


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name='Текст')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,  verbose_name='Автор')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return "Comment by " + self.author.user_name
