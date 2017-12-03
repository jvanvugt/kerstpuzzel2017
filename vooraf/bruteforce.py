import itertools
import string
with open('input.txt') as f:
    input = f.read().splitlines()

alphabet = list(string.ascii_lowercase)

for config in itertools.permutations('rgb'):
    try:
        sentence = []
        for word in input:
            letters = word.strip().split(' ')
            word = ''
            for letter in letters:
                word += alphabet[int(''.join([str(config.index(c)) for c in letter]), 3)]
            sentence.append(word)
        print(config)
        print(' '.join(sentence))
    except:
        continue

