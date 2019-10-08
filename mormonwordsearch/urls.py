from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.search, name='wordinput'),
    path('results/', views.results, name='your_word'),
    #path(r'^$', views.search)
]
