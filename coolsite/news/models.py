from django.db import models


class Artiles(models.Model):
    title = models.CharField('Назва', max_length=60)
    anons = models.CharField('Анонс', max_length=260)
    full_text = models.TextField('Текст')
    data = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    # таблиця категорій


class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=100)
    articles = models.ManyToManyField('Artiles', related_name='categories', verbose_name='Новини')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Tag(models.Model):
    name = models.CharField('Назва тегу', max_length=50)
    articles = models.ManyToManyField('Artiles', related_name='tags', verbose_name='Новини')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Author(models.Model):
    name = models.CharField('Ім\'я автора', max_length=100)
    articles = models.ManyToManyField('Artiles', related_name='authors', verbose_name='Новини')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
