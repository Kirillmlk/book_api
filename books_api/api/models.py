from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Author(AbstractBaseUser):
    """ Модель автора книги"""
    first_name = models.CharField(max_length=50, verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия автора")
    birth_date = models.DateField(verbose_name="Дата рождения автора")

    USERNAME_FIELD = 'id'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор книги")
    description = models.TextField(verbose_name="Описание книги")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")

    def __str__(self):
        return self.title