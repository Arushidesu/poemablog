from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('sobre/', views.sobre, name='sobre'),
    path('busca/', views.busca, name='busca'),
]