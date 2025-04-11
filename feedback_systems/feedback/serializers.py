from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'text', 'sentiment', 'created_at', 'status']
    
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Feedback text cannot be empty.")
        return value