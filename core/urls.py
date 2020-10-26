from django.urls import path

from .views import (
    article_list_function_based,
    article_detail_function_based,
    article_list_api_view_decorators,
    article_detail_api_view_decorators,
    ArticleAPIView,
    ArticleDetailAPIView,
)


urlpatterns = [
    # Function Based API Views
    path('function-based-articles/', article_list_function_based),
    path('function-based-article-detail/<int:pk>/',
         article_detail_function_based),

    # api_view() decorators
    path('api-view-decorators-articles/', article_list_api_view_decorators),
    path('api-view-decorators-article-detail/<int:pk>/', article_detail_api_view_decorators),

    # Class Based API Views
    path('class-based-articles/', ArticleAPIView.as_view()),
    path('class-based-article-detail/<int:id>/', ArticleDetailAPIView.as_view()),
]
