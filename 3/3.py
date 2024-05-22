import os

curr_dir = os.path.dirname(__file__)
infile_path = os.path.join(curr_dir, "input.txt")

with open(infile_path, 'r') as infile:
    text = infile.read().splitlines()

print(text)