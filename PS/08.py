# codewars - Stop gninnipS My sdroW!

import copy
def spin_words(sentence):
    li = sentence.split()
    rev_i = ''
    result = []
    for i in li:
        if len(i) >= 5:
            rev_i = i[::-1]
            result.append(copy.copy(rev_i))
        else:
            result.append(copy.copy(i))
    return ' '.join(result)

print(spin_words("Welcome"))