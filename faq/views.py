from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ

class FAQListView(APIView):
    def get(self, request):
        # Get the language from the query parameter (default is 'en')
        lang = request.query_params.get('lang', 'en')

        # Define a unique cache key based on the language
        cache_key = f'faqs_{lang}'

        # Try to fetch the data from the cache
        data = cache.get(cache_key)

        # If the data is not in the cache, fetch it from the database
        if not data:
            faqs = FAQ.objects.all()
            data = [
                {
                    'id': faq.id,
                    'question': faq.get_translated_question(lang),
                    'answer': faq.get_translated_answer(lang),
                }
                for faq in faqs
            ]

            # Store the data in the cache for 1 hour (3600 seconds)
            cache.set(cache_key, data, timeout=3600)

        # Return the cached or freshly fetched data as a response
        return Response(data)