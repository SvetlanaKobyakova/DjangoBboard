from django import forms
from django.contrib.auth.models import User



class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label='Заголовок')
    rooms = forms.IntegerField(label='Количество комнат')
    square = forms.IntegerField(label='Общая площадь квартиры')
    floor = forms.IntegerField(label='Этаж')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')
    city = forms.CharField(max_length=200, label='Город')
    metro = forms.CharField(max_length=200, label='Метро')
    street = forms.CharField(max_length=200, label='Улица')
    house = forms.CharField(max_length=200, label='Номер дома')
    apartment = forms.CharField(max_length=200, label='Номер квартиры')
    text = forms.CharField(widget=forms.Textarea, label='Описание объекта')
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
