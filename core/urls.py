from django.urls import path

from .views import article_list, article_detail


urlpatterns = [
    path('function-based-articles/', article_list),
    path('function-based-article-detail/<int:pk>/', article_detail),
]
