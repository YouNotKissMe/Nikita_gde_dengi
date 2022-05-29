from django.shortcuts import render
from .models import Anime


# Create your views here.

def main_animes(request):
    anime = Anime.objects.all()
    return render(request, 'all_anime.html', {'anime': anime})

def anime_page(request,pk):
    anime = Anime.objects.get(pk=pk)
    return render(request,'anime_page.html',{'anime':anime})