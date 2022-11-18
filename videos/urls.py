from django.urls import path
from . import views

urlpatterns = [
    path( '',views.gallery,name='gallery'),
    path( 'video/<str:pk>',views.viewVideo ,name='video'),
    path( 'add/', views.addVideos, name='add'),
]