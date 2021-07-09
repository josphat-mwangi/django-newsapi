from django.shortcuts import render
import requests
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
API_KEY = 'fd3949e9fc8d439f8d810573dc948437'

# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response= requests.get(url)
        data = response.json()
        articles = data['articles']
        page = request.GET.get('page', 1)
        paginator = paginator(articles, 5)

        try:
            users = paginator.page(page)
        except  PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
    elif category:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"
        response= requests.get(url)
        data = response.json()
        articles = data['articles']
        page = request.GET.get('page', 1)
        paginator = paginator(articles, 5)

        try:
            users = paginator.page(page)
        except  PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response= requests.get(url)
        data = response.json()
        articles = data['articles']

        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 5)

        try:
            users = paginator.page(page)
        except  PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

    context = {
        
        'users' : users
    }


    return render(request, 'newsapi/home.html', context)