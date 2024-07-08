from django.shortcuts import render
from .models import News_post


# Create your views here.
def page_news(request):
    all_news = News_post.objects.all()
    return render(request, 'news/news.html', {'all_news': all_news})
