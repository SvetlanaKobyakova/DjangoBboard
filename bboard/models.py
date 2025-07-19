from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from slugify import slugify


# описание модели поста
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    square = models.DecimalField(max_digits=4, decimal_places=1,verbose_name='Площадь квартиры')
    floor = models.IntegerField(verbose_name='Этаж')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость объекта')
    city = models.CharField(max_length=200,verbose_name='Адрес объекта')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=200, verbose_name='Номер дома')
    apartment = models.CharField(max_length=200,verbose_name='Номер квартиры')
    metro = models.CharField(max_length=200, verbose_name='Метро')
    text = models.TextField(verbose_name='Описание объекта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', editable=False)
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, editable=False, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        slug_title = slugify(self.title)
        slug = f'{slug_title}-{self.pk}'
        self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bboard:read_post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


# новая модель для загрузки несколько фото
class Photo(models.Model):
    image = models.ImageField(upload_to='upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id}"