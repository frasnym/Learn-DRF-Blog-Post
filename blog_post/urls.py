from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from core.views import ArticleViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    # path(r'api/core/', include('core.api.urls'), namespace='api-core')
    # path('api/', BlogPostRudView.as_view(), name='post-rud')

]