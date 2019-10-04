from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('wordinput/', views.wordinput, name='wordinput'),    
    path('your-word/', views.your_word, name='your_word')
]