import string

def preprocess_text(text):
    # Define a simple set of English stop words
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with',
         'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 
              'out', 'over', 'under', 'as', 'is', 'it', 'this', 'that',
      'these', 'those', 'am', 'are', 'was', 'were', 'be', 'been',
         'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'such', 
         'no', 'not', 'too', 'very', 'can', 'will', 'just', 'into', 'than', 
         'then', 'once', 'about', 'after', 'again', 'against', 'all', 'any', 
         'both', 'each', 'few', 'he', 'she', 'him', 'her', 'his', 'hers',
          'i', 'me', 'my', 'myself', 'our', 'ours', 'ourselves', 'you', 
          'your', 'yours', 'yourself', 'yourselves', 'they', 'them', 'their', 
          'theirs', 'themselves', 'we', 'us', 'what', 'which', 'who', 'whom', 
          'whose', 'why', 'how'
    }
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Split into words
    words = text.split()
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    # Join back into a string
    return ' '.join(filtered_words)

if __name__ == "__main__":
    input_text = input("Enter text: ")
    processed = preprocess_text(input_text)
    print("Processed text:", processed)

