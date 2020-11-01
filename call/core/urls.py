from django.urls import path

from call.core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search-user'),
]
