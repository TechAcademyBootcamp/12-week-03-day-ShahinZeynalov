from django.shortcuts import render
from random import randrange
from django.views.generic import ListView,DetailView
from .models import News
# Create your views here.

import requests
url=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=f8bbb8bd793d45d9b1df096734577194')
cont = url.json()
mylist = cont['articles'][:5]
def news_list(request):
    context={
    'mylist':mylist
    }
    return render(request,'news/news_list.html',context)

def news(request):
    rand=randrange(len(mylist))
    context={
    'news':mylist[rand]
    }

    return render(request,'news/news.html',context)

class NewsView(ListView):
    model = News
    template_name='news/list.html'
    context_object_name = 'news_list'

class DetailNews(DetailView):
    model = News
    template_name='news/detail_news.html'
