import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# Initialize the API client
client = Client()

class GetNewsItems(TestCase):
    """
    Test class for get news items
    """
    def setUp(self):
        pass

    def test_get_with_correct_params(self):
        chapters = ['news', 'sport', 'weather']
        news = [str(i) for i in range(2, 10)]
        for n in news:
            for chapter in chapters:
                # get API response
                request_url = "{}?chapter={}&news={}".format(reverse('get-news-item'), chapter, n)
                response = client.get(request_url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data['chapter'], chapter)
                self.assertEqual(len(response.data['news']), min(len(response.data['news']), int(n)))
    
    def test_empty_query_params(self):
        # first test with no query params
        request_url = reverse('get-news-item')
        response = client.get(request_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_with_incorrect_params(self):
        
        invalid_chapters = ['invalid', 'random', '']
        invalid_news = 0
        for chapter in invalid_chapters:
            # get API response
            request_url = "{}?chapter={}&news={}".format(reverse('get-news-item'), chapter, invalid_news)
            response = client.get(request_url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        