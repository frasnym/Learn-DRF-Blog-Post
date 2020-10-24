from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import viewsets, generics, mixins

from .models import Article
from .serializers import ArticleSerializer

"""
Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to 
mark the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views 
actually use more sensible behavior than this, but it'll do for our purposes right now.
"""
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


