from django.urls import path
from news_scrapper.views import news_view

urlpatterns = [
    path('', news_view, name="get-news-item"),
]
