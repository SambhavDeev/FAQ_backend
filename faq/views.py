from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = []
        for faq in faqs:
            data.append({
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            })
        return Response(data)