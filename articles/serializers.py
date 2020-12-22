from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """ List of articles"""
    content = serializers.SerializerMethodField()

    @staticmethod
    def get_content(article):
        return article.content[:700]

    class Meta:
        model = Article
        fields = ('title', 'content', 'url')


class DetailSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Article
        fields = ('title', 'content', 'url')

