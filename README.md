>📋 This system provides functions for suggesting corrections for misspelled words based on the minimum number of edits required to transform the misspelled word into a valid word from the vocabulary.

# Autocorrect system using Min Weighted Distance and Min Edit Distance

This autocorrect system employs Min Weighted Distance and Minimum Edit Distance algorithms to suggest corrections for misspelled words. Min Weighted Distance assigns different weights to various error types (substitution, insertion, deletion), calculating the weighted distance between the misspelled word and potential corrections. Minimum Edit Distance (Levenshtein Distance) measures the minimum number of single-character edits required to transform one word into another. The system maintains a dictionary of correct words, calculates distances to dictionary words for a given misspelled input, ranks potential corrections based on these distances, and suggests the word(s) with the lowest distance as the correction(s). This approach provides a balance between computational efficiency and accuracy in autocorrection suggestions.

## Abstract

This project implements a sophisticated autocorrect system that combines Min Weighted Distance and Minimum Edit Distance algorithms with probabilistic language modeling. The system aims to provide highly accurate spelling correction suggestions by leveraging both edit distance calculations and word frequency analysis from a given corpus. This hybrid approach allows for an optimal balance between computational efficiency and suggestion accuracy, making it suitable for real-time applications in various text-based interfaces.

## 1. Introduction

Autocorrect systems play a crucial role in modern text-based interfaces, significantly improving user experience by suggesting corrections for misspelled words. As digital communication continues to dominate both personal and professional spheres, the need for accurate and efficient autocorrect systems has never been greater.

This implementation explores an advanced approach that combines traditional edit distance algorithms with probabilistic methods to enhance suggestion accuracy. By considering both the structural similarity of words and their frequency of use, this system aims to provide more contextually appropriate and likely corrections.

### 1.1 Background

Traditional autocorrect systems often rely solely on edit distance metrics, which can lead to suggestions that, while structurally similar to the misspelled word, may not be the most likely or appropriate corrections. By incorporating probabilistic language modeling, this system addresses this limitation, providing a more nuanced approach to spelling correction.

### 1.2 Objectives

The primary objectives of this project are:
1. To implement an efficient edit distance calculation system for generating potential corrections
2. To integrate probabilistic language modeling based on corpus analysis
3. To combine these approaches for improved suggestion accuracy
4. To provide a real-time, interactive interface for demonstrating the system's capabilities

## 2. Methodology

### 2.1 Edit Distance Calculations

#### 2.1.1 Single Edit Distance
The `edit_one_letter` function forms the foundation of our edit distance calculations. It generates all possible words that are one edit away from the input word. The edits considered include:

- Deletion: Removing one letter from the word
- Insertion: Adding one letter to the word
- Replacement: Changing one letter to another
- Transposition: Swapping adjacent letters (optional, controlled by the `allow_switches` parameter)

This function is crucial for catching common typographical errors and minor misspellings.

#### 2.1.2 Double Edit Distance
The `edit_two_letters` function extends the single edit distance approach to generate words that are two edits away from the input word. This function is particularly useful for catching more complex misspellings that cannot be corrected with a single edit.

The implementation uses a nested approach, applying single edits to the results of the first round of edits. This comprehensive approach ensures a wide range of potential corrections are considered.

### 2.2 Minimum Edit Distance

The `min_edit_distance` function implements the Levenshtein Distance algorithm, a fundamental technique in string manipulation and spell checking. This dynamic programming approach efficiently computes the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another.

Key features of this implementation include:
- Customizable costs for insertion, deletion, and replacement operations
- Efficient matrix-based calculation using NumPy
- Return of both the cost matrix and the final minimum edit distance

This function provides a more nuanced measure of word similarity compared to simple edit counts, allowing for more accurate ranking of potential corrections.

### 2.3 Corpus Analysis

#### 2.3.1 Data Preprocessing
The system's vocabulary and word frequency data are derived from a provided text corpus (`words.txt`). The preprocessing pipeline includes:

1. Text Tokenization: The `preprocess_text` function reads the corpus file and tokenizes it into individual words, using regular expressions to handle various text formats.
2. Word Counting: The `get_count` function creates a dictionary of word frequencies, counting the occurrences of each unique word in the corpus.
3. Probability Calculation: The `get_probs` function converts raw word counts into probabilities, providing a measure of how likely each word is to appear in typical usage.

This preprocessing stage is crucial for building a representative model of language usage, which informs the system's correction suggestions.

#### 2.3.2 Probability Calculation
Word probabilities are calculated using the formula:

P(word) = count(word) / total_words

This simple yet effective approach provides a baseline measure of word likelihood, which is then used to rank and filter correction suggestions.

### 2.4 Suggestion Generation

Two main functions are responsible for generating and ranking suggestions:

1. `get_corrections`: This function combines edit distance calculations with word probabilities to suggest corrections. It follows these steps:
   - Generate potential corrections using single and double edit distance calculations
   - Filter suggestions to include only valid words from the vocabulary
   - Rank suggestions based on their probability of occurrence
   - Return the top N suggestions

2. `get_corrections_min_edit_distance`: This function uses the Minimum Edit Distance algorithm with additional weighting factors to generate suggestions. Its process includes:
   - Filtering the vocabulary to words within a specified edit distance of the input
   - Calculating a weighted score for each suggestion, combining edit distance and word probability
   - Ranking suggestions based on this composite score
   - Returning the top N suggestions

The combination of these two approaches allows the system to balance edit distance considerations with linguistic probability, leading to more accurate and contextually appropriate suggestions.

## 3. Implementation

The system is implemented in Python, leveraging the NumPy library for efficient matrix operations in the Minimum Edit Distance calculation. Key components of the implementation include:

- String Manipulation Functions: `delete_letter`, `insert_letter`, `switch_letter`, and `replace_letter` provide the basic operations for edit distance calculations.
- Edit Distance Calculations: `edit_one_letter` and `edit_two_letters` generate potential corrections.
- Minimum Edit Distance Algorithm: `min_edit_distance` efficiently computes the Levenshtein distance between words.
- Corpus Preprocessing: `preprocess_text`, `get_count`, and `get_probs` handle the analysis of the input corpus.
- Suggestion Generation: `get_corrections` and `get_corrections_min_edit_distance` combine the above components to produce ranked correction suggestions.
- Interactive Interface: The `main` function provides a simple command-line interface for testing the system.

## 4. Results and Discussion

The system demonstrates effective correction suggestions for a wide range of misspelled words, successfully balancing edit distance considerations with word probabilities. The inclusion of two-edit distance calculations allows for catching more complex misspellings, while the probabilistic approach helps prioritize more likely corrections.

## 5. Requirements

To install requirements:

```setup
pip install -r requirements.txt
```
To run program:

```setup
python main.py
```
![image](https://github.com/TrishamBP/autocorrect-nlp-python/assets/91331117/bfc5156a-3c41-45b7-a99c-3e19f2361140)


