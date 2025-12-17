from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/home.html', {
        'articles': articles
    })