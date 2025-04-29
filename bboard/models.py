from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# описание модели поста
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    square = models.FloatField(verbose_name='Площадь квартиры')
    floor = models.IntegerField(verbose_name='Этаж')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость объекта')
    city = models.CharField(max_length=200,verbose_name='Адрес объекта')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=200, verbose_name='Номер дома')
    apartment = models.CharField(max_length=200,verbose_name='Номер квартиры')
    metro = models.CharField(max_length=200, verbose_name='Метро')
    text = models.TextField(verbose_name='Описание объекта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    create_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', editable=False)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


