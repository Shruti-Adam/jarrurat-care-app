from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Volunteer
from .serializers import VolunteerSerializer

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [AllowAny]  # Allow anyone to register
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            volunteer = serializer.save()
            return Response({
                'success': True,
                'message': 'Thank you for registering as a volunteer!',
                'volunteer_id': volunteer.id,
                'next_steps': [
                    'You will receive an email confirmation',
                    'Our team will contact you within 48 hours',
                    'Please check your spam folder'
                ]
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)