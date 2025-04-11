from django.core.management.base import BaseCommand
from feedback.models import Feedback
from feedback.utils import analyze_sentiment

class Command(BaseCommand):
    help = 'Updates sentiment for existing feedback'

    def handle(self, *args, **kwargs):
        for feedback in Feedback.objects.filter(sentiment=''):
            feedback.sentiment = analyze_sentiment(feedback.text)
            feedback.save()
            self.stdout.write(self.style.SUCCESS(f'Updated: {feedback.text} -> {feedback.sentiment}'))