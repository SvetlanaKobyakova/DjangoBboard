from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               error_messages={
                                   'required': 'Пожалуйста, введите логин'
                               },
                               widget=forms.TextInput(attrs={"class":"myfield"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class":"myfield"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"class":"myfield"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={"class":"myfield"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class":"myfield"}))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={"class":"myfield"}),
                                error_messages={
                                    'required': 'Пожалуйста, подтвердите пароль'
                                })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

class NewRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               error_messages={
                                   'required': 'Пожалуйста, введите логин'
                               },
                               widget=forms.TextInput(attrs={"class": "myfield"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": "myfield"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"class": "myfield"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={"class": "myfield"}))
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "myfield"}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={"class":"myfield"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
        help_texts = {
            'username': ''
        }
    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cleaned_data['password2']


class CustomPasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        label='Старый пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomlete': 'current-password', 'autofocus': True, 'class': 'myfield_old_password'}
        ),
    )
    new_password1 = forms.CharField(
        label='Новый пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'myfield_new_password1'})
    )
    new_password2 = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'myfield_new_password2'})
    )
    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if old_password and new_password1:
            if old_password == new_password1:
                raise ValidationError('Новый пароль должен отличаться от старого')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError('Введенные пароли не совпадают')

        return cleaned_data

