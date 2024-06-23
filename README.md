>📋 This system provides functions for suggesting corrections for misspelled words based on the minimum number of edits required to transform the misspelled word into a valid word from the vocabulary.

# Autocorrect system using Min Weighted Distnce and Min Edit Distance

This autocorrect system employs Min Weighted Distance and Minimum Edit Distance algorithms to suggest corrections for misspelled words. Min Weighted Distance assigns different weights to various error types (substitution, insertion, deletion), calculating the weighted distance between the misspelled word and potential corrections. Minimum Edit Distance (Levenshtein Distance) measures the minimum number of single-character edits required to transform one word into another. The system maintains a dictionary of correct words, calculates distances to dictionary words for a given misspelled input, ranks potential corrections based on these distances, and suggests the word(s) with the lowest distance as the correction(s). This approach provides a balance between computational efficiency and accuracy in autocorrection suggestions.

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

