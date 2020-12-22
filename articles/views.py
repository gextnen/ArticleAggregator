from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer, DetailSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = DetailSerializer
