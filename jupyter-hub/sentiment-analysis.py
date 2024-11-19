from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text.
    Returns the polarity and subjectivity scores and a sentiment label.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "Polarity": polarity,
        "Subjectivity": subjectivity,
        "Sentiment": sentiment
    }

if __name__ == "__main__":
    # Open and read the text file
    file_path = 'example.txt'
    with open(file_path, 'r') as file:
        text = file.read()

    # Analyze sentiment
    result = analyze_sentiment(text)

    # Display results
    print("\nSentiment Analysis Results:")
    print(f"Polarity: {result['Polarity']:.2f}")
    print(f"Subjectivity: {result['Subjectivity']:.2f}")
    print(f"Sentiment: {result['Sentiment']}")