from django.contrib import admin

from .models import Article, Tag, Type
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'update_time', 'type', 'isActive', 'view_count']
    list_display_links = ['title']

    
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['name']