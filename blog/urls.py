from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('article/<int:id>', views.article, name='article'),
    path('post/', views.add_article, name='post'),
]