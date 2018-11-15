from django.shortcuts import render

# Create your views here.


##首页

def index(requests):
    return render(requests,'news/index.html')

def search(requests):
    return render(requests,'news/search.html')

