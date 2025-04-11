from rest_framework import serializers
from .models import Feedback
from .utils import analyze_sentiment

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'text', 'sentiment', 'created_at', 'status']
    
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Feedback text cannot be empty.")
        return value
    
    def create(self, validated_data):
        # Apply sentiment analysis before saving
        text = validated_data['text']
        validated_data['sentiment'] = analyze_sentiment(text)
        return super().create(validated_data)