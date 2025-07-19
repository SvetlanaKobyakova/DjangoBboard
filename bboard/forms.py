from django import forms
from django.contrib.auth.models import User
from .models import Post
from .models import Photo


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
        # получаем author из именованных аргументов (его передали во views)
        if kwargs.get('initial'):
            author = kwargs['initial'].pop('author')
        else:
            author = kwargs.pop('author')
        # вызываем конструктор родительсого
        super().__init__(*args, **kwargs)
        # устанавливаем начальное значение поля author
        self.fields['author'].initial = author
        # отключаем видимость этого поля в форме
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('title', 'rooms','square',
                  'floor', 'price','city',
                  'metro', 'street', 'house',
                  'apartment', 'text', 'image',
                  'author',
                  'phone_number',
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
            'image': 'Изображение',
            'phone_number': 'Номер телефона',
        }

class FilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(),
                                    label='Автор',
                                    required=False)
    created_at = forms.DateField(label='Дата публикации',
                                 widget=forms.DateInput(attrs={'type': 'date'}),
                                 input_formats=['%Y-%m-%d'],
                                 required=False)

    # новая форма для загрузки несколько фото
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # Разрешаем выбор нескольких файлов

class MultiplePhotoForm(forms.ModelForm):
    image = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        label='Выберите фото',
        help_text='Можно выбрать несколько файлов'
    )

    class Meta:
        model = Photo
        fields = ['image']
