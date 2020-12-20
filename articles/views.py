from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticlesView(ListView):
    """Список статей"""
    model = Article
    template_name = 'article_list.html'
