from textblob import TextBlob

def analyze_sentiment(text):
    # Get polarity (-1 to 1: negative to positive)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Check for urgent keywords 
    urgent_keywords = ['dirty', 'broken', 'urgent', 'emergency', 'not working']
    is_urgent = any(keyword in text.lower() for keyword in urgent_keywords)

    if is_urgent:
        return 'Urgent'
    elif polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'  # Fallback for neutral/unclear