from django.urls import path
from .views import ArticleAPIView, DetailAPIView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:pk>/', DetailAPIView.as_view()),
]
