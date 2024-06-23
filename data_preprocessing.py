import re


# Function to read a text files and get all the words
def preprocess_text(file_name):
    with open(file_name) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+', file_name_data)

    return words


# Get count function, calculates how many times a word has appeared
def get_count(word_l):
    word_count_dict = {}  # fill this with word counts
    for word in word_l:
        if word in word_count_dict:
            # If the word is already in the dictionary, increment its count by 1
            word_count_dict[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            word_count_dict[word] = 1
    return word_count_dict


# Given the dictionary of word counts, compute the probability that each word will appear if randomly selected from
# the corpus of words.
def get_probs(word_count_dict):
    probs = {}  # return this variable correctly
    m = sum(word_count_dict.values())
    for key in word_count_dict.keys():
        probs[key] = word_count_dict[key] / m
    # get the total count of words for all words in the dictionary
    return probs
