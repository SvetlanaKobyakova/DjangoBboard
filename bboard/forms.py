from django import forms
from django.contrib.auth.models import User



class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    rooms = forms.IntegerField()
    square = forms.IntegerField()
    floor = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    address = forms.CharField(max_length=500)
    metro = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all())
