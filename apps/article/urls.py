from django.urls import path

from .views import home, single, home_2, article


urlpatterns = [
    path('', home, name='home'),
    path('single/<slug:slug>/', single, name='single'),
    path('home_2/', home_2, name='home_2'),
    path('article/', article, name='article'),
]
