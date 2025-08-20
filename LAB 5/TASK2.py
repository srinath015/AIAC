def analyze_sentiment(text):
    positive_words = ['awesome', 'good', 'great', 'excellent', 'fantastic', 'amazing', 'happy', 'love']
    negative_words = ['worst', 'bad', 'terrible', 'awful', 'sad', 'hate', 'poor', 'disappointing']

    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        sentiment = 'positive sentiment'
    elif neg_count > pos_count:
        sentiment = 'negative sentiment'
    else:
        sentiment = 'neutral sentiment'
    return sentiment

if __name__ == "__main__":
    user_input = input("Enter a sentence for sentiment analysis: ")
    result = analyze_sentiment(user_input)
    print(result)