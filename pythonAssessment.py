import string

def count_specific_word(text, word):
    count = text.lower().split().count(word.lower())
    print(f"The word '{word}' appears {count} time(s).")
    return count

def identify_most_common_word(text):
    if not text or text.isspace():
        return None
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_common = max(word_count, key=word_count.get)
    print(f"The most common word is '{most_common}'.")
    return most_common

def calculate_average_word_length(text):
    if not text or text.isspace():
        return 0
    words = text.lower().split()
    cleaned_words = [''.join(c for c in w if c not in string.punctuation) for w in words]
    cleaned_words = [w for w in cleaned_words if w]
    if not cleaned_words:
        return 0
    average = sum(len(w) for w in cleaned_words) / len(cleaned_words)
    print(f"The average word length is {average:.2f}.")
    return average

def count_paragraphs(text):
    if not text or text.isspace():
        return 1
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text):
    if not text or text.isspace():
        return 1
    return sum(1 for c in text if c in '.!?') or 1

def analyze_article(text):
    if not text or text.isspace():
        print("Error: No text provided.")
        return
    
    print("\n=== ARTICLE ANALYSIS ===\n")
    print(f"Words: {len(text.lower().split())}")
    print(f"Paragraphs: {count_paragraphs(text)}")
    print(f"Sentences: {count_sentences(text)}\n")
    identify_most_common_word(text)
    calculate_average_word_length(text)
    print()

if __name__ == "__main__":
    while True:
        print("1. Analyze article\n2. Search word\n3. Exit")
        choice = input("Choose (1-3): ").strip()
        
        if choice == "1":
            print("Enter article text:")
            text = input()
            analyze_article(text)
        
        elif choice == "2":
            text = input("Enter article: ")
            word = input("Enter word to search: ")
            count_specific_word(text, word)
            print()
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.\n")