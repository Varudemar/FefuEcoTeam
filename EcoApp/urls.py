from django.urls import path

from . import views

urlpatterns = [
    path('articles', views.articles, name='articles'),
    path('articles/<int:id>/', views.singlearticle, name='single'),
    path('', views.promotions, name='promotions'),
    path('promotion/<int:id>/', views.singlepromotion, name='promotion'),
]
