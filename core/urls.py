from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    article_list_function_based,
    article_detail_function_based,
    article_list_api_view_decorators,
    article_detail_api_view_decorators,
    ArticleAPIView,
    ArticleDetailAPIView,
    GenericRAPIView,
    GenericCRAPIView,
    GenericCRUDAPIView,
    ArticleViewSet,
    ArticleGenericViewSet,
)

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'article-generic', ArticleGenericViewSet, basename='article-generic')


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

    # Generic & Mixin API View
    path('generic-mixin-article-list/', GenericRAPIView.as_view()),
    path('generic-mixin-article-CR/', GenericCRAPIView.as_view()),
    path('generic-mixin-article-CRUD/<int:id>/', GenericCRUDAPIView.as_view()),

    # ViewSet
    path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)), # ! This is not needed
]
