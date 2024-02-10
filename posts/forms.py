from django import forms
from .models import Category
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User

class UserLogin(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
class NewsForms(forms.Form):
    title = forms.CharField(max_length=150)
    context = forms.CharField()
    is_publish =  forms.BooleanField(initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())