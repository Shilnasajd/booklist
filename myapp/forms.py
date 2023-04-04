from django import forms #forms.py
from myapp.models import Books
from django.contrib.auth.models import User
class BookForm(forms.Form):
    
    name=forms.CharField(label="Book Name",required=True)
    author=forms.CharField(label="Book Author",required=True)
    price=forms.CharField(label="Price",required=True)

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["name","author","price"]

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"})
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))