from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('game/', views.game, name='game')
]
