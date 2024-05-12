import os

# Get the directory of the current script and path of the input
script_dir = os.path.dirname(__file__)

# Helper module
from util import find_digit, find_word

"""
Solution Part A:
For each line, read it forward to find the first digit, then backward to find the last digit
Runtime: O(N) for N number of lines
"""
input_file_path = os.path.join(script_dir, 'input.txt')
result = 0
with open(input_file_path, 'r') as infile:
    for line in infile:
        line = line[:-1]

        d1 = find_digit(line)[1]
        d2 = find_digit(line, from_start=False)[1]

        # Add to the cumulative
        result += int(str(d1) + str(d2))
print("Part A Solution:", result)

"""
Solution Part B:
For each line, read it forward to find the first digit and first numeric word, then backward for the last digit and last word. Utilize min and max on their indices to find the earliest number to use in the sum. 
Runtime: O(10*N) = O(N) for N number of lines. Ugly 10 constant but nkoShrug
"""
input_file_path = os.path.join(script_dir, 'input.txt')
numbers_key = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
numbers_spelled_out = list(numbers_key.keys())
result = 0
with open(input_file_path, 'r') as infile:
    for line in infile:
        line = line[:-1]

        # Find the first and last indices of each digit
        first_digit_pair = find_digit(line)
        last_digit_pair = find_digit(line, from_start=False)

        # Find the first and last indices of each number word
        first_word_pairs = []
        last_word_pairs = []
        for word in numbers_spelled_out:
            idx_first_word, idx_last_word = find_word(line, word), find_word(line, word, from_start=False)
            if idx_first_word:
                first_word_pairs.append(idx_first_word)
            if idx_last_word:
                last_word_pairs.append(idx_last_word)
        
        # Determine the first and last numbers, either in digit or word form, occurring in the line 
        p1 = min(
            [pair for pair in [first_digit_pair] + first_word_pairs if pair],
            key=lambda pair: pair[0]
        )[1]
        p1 = numbers_key[p1] if isinstance(p1, str) else p1
        p2 = max(
            [pair for pair in [last_digit_pair] + last_word_pairs if pair],
            key=lambda pair: pair[0]
        )[1] 
        p2 = numbers_key[p2] if isinstance(p2, str) else p2

        # Add to the cumulative
        result += int(str(p1) + str(p2))
 
print("Part B Solution:", result)
