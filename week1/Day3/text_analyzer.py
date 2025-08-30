import re
from collections import Counter

def analyze_text(text):
    # Handle empty input
    if not text.strip():
        return {
            "word_count": 0,
            "sentence_count": 0,
            "most_frequent_word": ("None", 0)
        }

    # Word count
    words = text.split()
    word_count = len(words)

    # Sentence count
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]  # Remove empty strings
    sentence_count = len(sentences)

    # Most frequent word (case-insensitive)
    words_lower = text.lower().split()
    word_freq = Counter(words_lower)
    most_common = word_freq.most_common(1)
    most_frequent_word = most_common[0] if most_common else ("None", 0)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "most_frequent_word": most_frequent_word
    }

def save_report(results, filename="analysis_report.txt"):
    with open(filename, "w") as f:
        f.write(f"Word Count: {results['word_count']}\n")
        f.write(f"Sentence Count: {results['sentence_count']}\n")
        f.write(f"Most Frequent Word: {results['most_frequent_word'][0]} ({results['most_frequent_word'][1]} times)\n")

def main():
    # Get user input
    print("Text Analyzer CLI App")
    text = input("Enter a paragraph (or press Enter to finish): ")

    # Analyze text
    results = analyze_text(text)

    # Print results
    print("\nAnalysis Results:")
    print(f"Word Count: {results['word_count']}")
    print(f"Sentence Count: {results['sentence_count']}")
    print(f"Most Frequent Word: {results['most_frequent_word'][0]} ({results['most_frequent_word'][1]} times)")

    # Save to file
    save_report(results)
    print(f"\nResults saved to 'analysis_report.txt'")

if __name__ == "__main__":
    main()