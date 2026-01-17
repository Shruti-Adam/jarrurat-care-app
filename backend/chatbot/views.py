from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from datetime import datetime
from .services import HealthcareChatbot

class ChatbotAPI(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    
    def post(self, request):
        # Try to get message from JSON or form data
        message = request.data.get('message', '')
        
        if isinstance(message, list):
            message = message[0] if message else ''
        
        message = str(message).strip()
        
        if not message:
            return Response({'error': 'Message is required'}, status=400)
        
        chatbot = HealthcareChatbot()
        response = chatbot.get_response(message)
        
        return Response({
            'success': True,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
    
    def get(self, request):
        """GET method for testing"""
        return Response({
            'info': 'Healthcare Chatbot API',
            'usage': 'POST a JSON with {"message": "your question"}',
            'example_questions': [
                'How can I volunteer?',
                'What services do you provide?',
                'How to donate?',
                'Contact information',
                'What is your impact?'
            ]
        })