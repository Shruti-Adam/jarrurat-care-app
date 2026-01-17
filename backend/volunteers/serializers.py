from rest_framework import serializers
from .models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):
    skills_display = serializers.CharField(source='get_skills_display', read_only=True)
    
    class Meta:
        model = Volunteer
        fields = ['id', 'name', 'email', 'phone', 'skills', 'skills_display', 
                  'hours_per_week', 'motivation', 'created_at']
        extra_kwargs = {
            'email': {'required': True},
            'hours_per_week': {'min_value': 1, 'max_value': 40}
        }