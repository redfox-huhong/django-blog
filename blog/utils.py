"""
utils.py
"""

from django.forms.models import model_to_dict

def tag_model_to_dict(tag) -> dict:
    """
    将标签模型对象转换为字典
    """
    tag_dict = model_to_dict(tag)
    return tag_dict

def article_model_to_dict(article, max_length=0) -> dict:
    """
    将文章模型对象转换为字典
    max_length: 截取文章内容长度，默认为0表示不截取。
    """
    article_dict = model_to_dict(article)
    article_dict['user'] = article.user.username
    article_dict['type'] = article.type.name
    article_dict['create_time'] = article.create_time.strftime('%Y-%m-%d')
    article_dict['update_time'] = article.update_time.strftime('%Y-%m-%d')
    article_dict['tags'] = [tag_model_to_dict(tag)['name'] for tag in article_dict['tags']]
    if max_length:
        article_dict['content'] = article_dict['content'][:max_length + 1] + '....'
    return article_dict