from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

from .models import Article, Type, Tag
from .utils import article_model_to_dict



# Create your views here.

def articles(request):
    data = {
            'status': 0,
            'message': 'fail',
    } 
    try:
        articles_rect = Article.objects.all().filter(isActive=True)
        articles = [article_model_to_dict(article, 80) for article in articles_rect]
        data['status'] = 1
        data['message'] = 'success'
        data['articles'] = articles
    except Exception as e:
        print(e)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})


def article(request, id):
    data = {
            'status': 0,
            'message': 'fail',
    } 
    try:
        article = Article.objects.get(pk=id)
        data['status'] = 1
        data['message'] = 'success'
        data['article'] = article_model_to_dict(article)
    except Exception as e:
        print(e)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})

def add_article(request):
    data = {
        'status': 0,
        'message': 'fail',
    }
    if request.method == 'POST':
        post_dict = {}
        post_dict['title'] = request.POST.get('title')
        post_dict['content'] = request.POST.get('content')
        post_dict['user'] = User.objects.get(pk=request.POST.get('user'))
        post_dict['type'] = Type.objects.get(pk=request.POST.get('type')) 
        tags = Tag.objects.filter(pk__in=[tag for tag in request.POST.get('tags').split(',')])
        article = Article(**post_dict)
        try:
            article.save()
            article.tags.set(tags)
            data['status'] = 1
            data['message'] = 'success'
        except Exception as e:
            print(e)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})

def del_article(request, id):
    data = {
        'status': 0,
        'message': 'fail',
    }
    try:
        pk = request.POST.get('id')
        req = Article.objects.get(pk=id)
        if not req:
            data['message'] = 'no match data'
        req.isActive=False
        req.save()
    except Exception as e:
        print(e)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})
        
