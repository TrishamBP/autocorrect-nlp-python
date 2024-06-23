# delete_letter: given a word, it returns all the possible strings that have one character removed.
def delete_letter(word, verbose=False):
    delete_l = []
    split_l = []
    for c in range(len(word)):
        split_l.append((word[:c], word[c:]))
    for a, b in split_l:
        delete_l.append(a + b[1:])
    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
    return delete_l


# switch_letter: given a word, it returns all the possible strings that have two adjacent letters switched.
def switch_letter(word, verbose=False):
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    switch_l = [a + b[1] + b[0] + b[2:] for a, b in split_l if len(b) >= 2]
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")
    return switch_l


# replace_letter: given a word, it returns all the possible strings that have one character replaced by another different letter.
def replace_letter(word, verbose=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []
    for c in range(len(word)):
        split_l.append((word[0:c], word[c:]))
    replace_l = [a + l + (b[1:] if len(b) > 1 else '') for a, b in split_l if b for l in letters]
    replace_set = set(replace_l)
    replace_set.remove(word)
    # turn the set back into a list and sort it, for easier viewing
    replace_l = sorted(list(replace_set))
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")
    return replace_l


# insert_letter: given a word, it returns all the possible strings that have an additional character inserted.
def insert_letter(word, verbose=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    insert_l = [a + c + b for a, b in split_l for c in letters]
    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    return insert_l
