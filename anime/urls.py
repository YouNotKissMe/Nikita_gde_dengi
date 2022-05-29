from django.urls import path
from .views import main_animes,anime_page

urlpatterns = [
    path('', main_animes, name='all_anime'),
    path('<int:pk>/',anime_page,name='anime_page')
]