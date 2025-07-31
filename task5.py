def count_word_frequency():
    text = input("Enter a string: ")
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    for word, count in freq.items():
        print(f"'{word}': {count}")

count_word_frequency()