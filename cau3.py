import re

def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter

file_path = 'P1_data.txt'
try:
    result = count_word(file_path)
    print(result['man'])
    assert result['who'] == 3
except FileNotFoundError as e:
    print(e)