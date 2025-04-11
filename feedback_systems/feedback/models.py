from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20, blank=True)  # Positive, Negative, Urgent
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # Pending, Escalated, Resolved

    def __str__(self):
        return f"{self.text} ({self.sentiment})"