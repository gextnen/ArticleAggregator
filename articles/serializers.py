from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """ List of articles"""
    class Meta:
        model = Article
        fields = ['title', 'content', 'url']
