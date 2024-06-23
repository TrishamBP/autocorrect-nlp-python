from data_preprocessing import preprocess_text, get_count, get_probs
from combined_edit_functions import *

word_l = preprocess_text('./words.txt')
vocab = set(word_l)  # this will be your new vocabulary
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")

word_count_dict = get_count(word_l)
print(f"There are {len(word_count_dict)} key values pairs")
print(f"The count for the word 'apple' is {word_count_dict.get('apple', 0)}")

probs = get_probs(word_count_dict)
print(f"Length of probs is {len(probs)}")
print(f"P('apple') is {probs['apple']:.4f}")


def get_corrections(word, probs, vocab, n=2, verbose=False):
    # Step 1: create suggestions as described above    
    suggestions = list(
        (word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(
            vocab))

    # Step 2: determine probability of suggestions
    n_best = [[s, probs.get(s, 0)] for s in suggestions]

    # Step 3: Get all your best words and return the most probable top n_suggested words as n_best
    n_best.sort(key=lambda x: x[1], reverse=True)

    # Select the top n most probable suggestions
    n_best = n_best[:n]

    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best


def get_corrections_min_edit_distance(word, probs, vocab, n=2):
    # Use minimum edit distance and consider additional factors

    # 1. Minimum Edit Distance Filtering:
    suggestions = [w for w in vocab if min_edit_distance(word, w)[1] <= 2]  # Consider words within 2 edit distance

    # 2. Additional Considerations (optional):
    #    - Word frequency: prioritize suggestions with higher probability from `probs`
    weighted_suggestions = []
    for suggestion in suggestions:
        edit_distance = min_edit_distance(word, suggestion)[1]
        word_prob = probs.get(suggestion, 0)  # Handle unseen words with probability 0
        # Combine edit distance and probability using a weighting factor (alpha)
        alpha = 0.7  # Experiment with different weights between 0 and 1
        weighted_score = (1 - alpha) * edit_distance + alpha * word_prob
        weighted_suggestions.append((suggestion, weighted_score))

    # 3. Sorting based on Combined Criteria:
    weighted_suggestions.sort(key=lambda x: x[1])  # Sort by weighted score (ascending)

    return weighted_suggestions[:n]  # Return the top n suggestions


def main():
    """Main function for interactive autocorrect usage."""

    while True:
        user_word = input("Enter a word (or 'q' to quit): ")
        if user_word.lower() == 'q':
            break

        suggestions = get_corrections_min_edit_distance(user_word, probs, vocab) + get_corrections(user_word, probs, vocab)

        if suggestions:
            print(f"Did you mean:")
            for suggestion, _ in suggestions:
                print(f"- {suggestion}")  # Only print the suggestion (no probability for brevity)
        else:
            print("No suggestions found.")


if __name__ == "__main__":
    main()
