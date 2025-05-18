from django import forms
from django.contrib.auth.models import User
from .models import Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label='Заголовок')
#     rooms = forms.IntegerField(label='Количество комнат')
#     square = forms.IntegerField(label='Общая площадь квартиры')
#     floor = forms.IntegerField(label='Этаж')
#     price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')
#     city = forms.CharField(max_length=200, label='Город')
#     metro = forms.CharField(max_length=200, label='Метро')
#     street = forms.CharField(max_length=200, label='Улица')
#     house = forms.CharField(max_length=200, label='Номер дома')
#     apartment = forms.CharField(max_length=200, label='Номер квартиры')
#     text = forms.CharField(widget=forms.Textarea, label='Описание объекта')
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
#     image = forms.ImageField(required=False, label='Изображение')

class PostForm(forms.ModelForm):
    # дополняем конструктор родительского класса
    def __init__(self, *args, **kwargs):
        # получаем author из именованных аргументов (его передали во views
        author = kwargs.pop('author')
        # вызываем конструктор родительсого
        super().__init__(*args, **kwargs)
        # устанавливаем начальное значение поля author
        self.fields['author'].initial = author
        # отключаем видимость этогополя в форме
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('title', 'rooms','square',
                  'floor', 'price','city',
                  'metro', 'street', 'house',
                  'apartment', 'text', 'image',
                  'author'
                  )

        labels = {
            'title': 'Заголовок',
            'rooms': 'Количество комнат',
            'square': 'Общая площадь квартиры',
            'floor': 'Этаж',
            'price': 'Цена',
            'city': 'Город',
            'metro': 'Метро',
            'street': 'Улица',
            'house': 'Номер дома',
            'apartment': 'Номер квартиры',
            'text': 'Описание объекта',
            'image': 'Изображение'
        }
