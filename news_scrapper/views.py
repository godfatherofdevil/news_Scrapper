from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from news_scrapper.get_news_items import get_items

@api_view(['GET'])
def news_view(request):

    if request.method == "GET":
        # get the query params from the url
        chapter = request.query_params.get("chapter", None)
        news = request.query_params.get("news", None)
        response_ = {}

        if (chapter is not None) and (news is not None):
            news_items = get_items(chapter=chapter, n_items=news)
            if not isinstance(news_items, list):
                return Response({'error': news_items}, status=HTTP_500_INTERNAL_SERVER_ERROR)
            elif not news_items:
                return Response({'error': 'incorrect query params, please check'}, status=HTTP_400_BAD_REQUEST)
        else:
            error = "Make a request with chapter and news query params set"
            return Response({"error": error}, status=HTTP_400_BAD_REQUEST)
        
        # create the response dictionary
        response_['chapter'] = chapter
        response_['news'] = []

        for item in news_items:
            response_['news'].append({"title": item[0], "URL": item[1]})
        
        return Response(response_, status=HTTP_200_OK)
