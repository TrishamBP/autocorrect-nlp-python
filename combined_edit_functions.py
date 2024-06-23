import numpy as np
from string_manipulations import delete_letter, insert_letter, switch_letter, replace_letter


# Implement the edit_one_letter function to get all the possible edits that are one edit away from a word. The edits
# consist of the replace, insert, delete, and optionally the switch operation. You should use the previous functions
# you have already implemented to complete this function. The 'switch' function is a less common edit function,
# so its use will be selected by an "allow_switches" input argument.
def edit_one_letter(word, allow_switches=True):
    edit_one_set = set()
    edit_one_set.update(delete_letter(word))
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    return set(edit_one_set)


tmp_word = "at"
tmp_edit_one_set = edit_one_letter(tmp_word)
# turn this into a list to sort it, in order to view it
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
print(f"Number of outputs from edit_one_letter('at') is {len(edit_one_letter('at'))}")


# edit_two_letters function that returns a set of words that are two edits away. Note that creating additional edits
# based on the edit_one_letter function may 'restore' some one_edits to zero or one edits. That is allowed here. This
# is accounted for in get_corrections.
def edit_two_letters(word, allow_switches=True):
    edit_two_set = set()
    edit_one = edit_one_letter(word, allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w, allow_switches=allow_switches)
            edit_two_set.update(edit_two)
    return set(edit_two_set)


tmp_edit_two_set = edit_two_letters("a")
tmp_edit_two_l = sorted(list(tmp_edit_two_set))
print(f"Number of strings with edit distance of two: {len(tmp_edit_two_l)}")
print(f"First 10 strings {tmp_edit_two_l[:10]}")
print(f"Last 10 strings {tmp_edit_two_l[-10:]}")
print(f"The data type of the returned object should be a set {type(tmp_edit_two_set)}")
print(f"Number of strings that are 2 edit distances from 'at' is {len(edit_two_letters('at'))}")


def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    """Calculates the minimum edit distance between two strings.

    Args:
        source (str): The source string.
        target (str): The target string.
        ins_cost (int, optional): The cost of inserting a character. Defaults to 1.
        del_cost (int, optional): The cost of deleting a character. Defaults to 1.
        rep_cost (int, optional): The cost of replacing a character. Defaults to 2.

    Returns:
        tuple: A tuple containing the cost matrix and the minimum edit distance.
    """

    m = len(source)
    n = len(target)

    # Initialize cost matrix with zeros
    D = np.zeros((m + 1, n + 1), dtype=int)

    # Fill in the first row (costs of deleting from source)
    for row in range(1, m + 1):
        D[row, 0] = D[row - 1, 0] + del_cost

    # Fill in the first column (costs of inserting into target)
    for col in range(1, n + 1):
        D[0, col] = D[0, col - 1] + ins_cost

    # Fill in the rest of the cost matrix
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            # Minimum cost of: inserting, deleting, or replacing
            insert_cost = D[row, col - 1] + ins_cost
            delete_cost = D[row - 1, col] + del_cost
            replace_cost = D[row - 1, col - 1] + (source[row - 1] != target[col - 1]) * rep_cost
            D[row, col] = min(insert_cost, delete_cost, replace_cost)

    return D, D[m, n]  # Return the cost matrix and the minimum edit distance
