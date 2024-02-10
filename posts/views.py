from django.shortcuts import render, redirect
from .models import *
from .forms import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# users
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,  'вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request , 'error')
    else:
        form =  UserRegister()
    return render(request , 'register.html', {'form':form})

def userLogin(request):
    if request.method == 'POST':
        form = UserLogin(data = request.POST)
        if form.is_valid():
           user = form.get_user()
           login(request , user)
           return redirect('/')
    else:
        form = UserLogin()
    return render(request , 'login.html', {'form':form})

def userClose(request):
    logout(request)
    return redirect('login')

# Create your views here.
def index(request):
    news = News.objects.order_by('-create_add')
    category = Category.objects.all()
    context = {
        'news':news,
        'category':category,
        
    }
    return render(request , 'index.html', context)

def get_category(request , category_id):
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.all()
    categories = Category.objects.get(id = category_id)
    context = {
        'news':news,
        'category':category,
        'categories':categories
    }
    return render(request , 'category.html' , context)

def add_news(request):
    if request.method == 'POST':
        form = NewsForms(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            # news = form.save()
            return redirect('/')
    else:
        form = NewsForms()
    return render(request , 'add_news.html',{'form':form})

def delete_news(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        news = News.objects.get(id=id)
        news.delete()
        return redirect('/')
    context ={
        'news':news
    }
    return render(request, 'news_delete.html', context)


def getIdNews(request, id):
    news = News.objects.get(id = id)
    context={
        "news":news
    }
    return render(request, 'news_id.html', context)
    
