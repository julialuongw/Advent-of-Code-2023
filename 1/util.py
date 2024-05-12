
"""
Returns a tuple of the index of the first or last digit in a string and the digit itself -- (idx, digit). If none are present, return None
"""
def find_digit(s: str, from_start=True) -> tuple[int,int]:
    if from_start:
        start_idx = 0
        end_idx = len(s)
        step = 1
    else:
        start_idx = len(s)-1
        end_idx = -1
        step = -1

    for i in range(start_idx, end_idx, step):
        ch = s[i]
        if ch.isdigit():
            return (i, int(ch))
    
    return None

"""
Returns a tuple of the index of a given word's first or last occurrence in a string and the word itself -- (idx, word). If none are present, return None
"""
def find_word(s: str, word: str, from_start=True) -> tuple[int,str]:
    if from_start:
        start_idx = 0
        end_idx = len(s) - len(word) + 1
        step = 1
    else:
        start_idx = len(s) - len(word)
        end_idx = -1
        step = -1

    for i in range(start_idx, end_idx, step):
        window = s[i : i + len(word)]
        if window == word:
            return (i, word)
    
    return None

