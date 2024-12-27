from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artist/new/', views.artist_create, name='artist_create'),
    path('artist/<int:pk>/edit/', views.artist_update, name='artist_update'),
    path('artist/<int:pk>/delete/', views.artist_delete, name='artist_delete'),
    path('paintings/', views.painting_list, name='painting_list'),
    path('painting/<int:pk>/', views.painting_detail, name='painting_detail'),
    path('painting/new/', views.painting_create, name='painting_create'),
    path('painting/<int:pk>/edit/', views.painting_update, name='painting_update'),
    path('painting/<int:pk>/delete/', views.painting_delete, name='painting_delete'),
]