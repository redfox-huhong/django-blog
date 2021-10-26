from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('article/<int:id>', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('del_article/<int:id>', views.del_article, name='del_article'),
]