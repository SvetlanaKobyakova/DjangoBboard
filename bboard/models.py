from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# описание модели поста
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    square = models.FloatField(verbose_name='Площадь квартиры')
    floor = models.IntegerField(verbose_name='Этаж')
    price = models.FloatField(verbose_name='Стоимость объекта')
    text = models.TextField(verbose_name='Описание объекта')
    address = models.TextField(verbose_name='Адрес объекта')
    metro = models.CharField(max_length=200, verbose_name='Метро')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    create_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', editable=False)


