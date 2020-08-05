from pprint import pprint


mess = open('pc2.txt').read()


characters = {}

for char in mess:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

print(sorted(characters, key=lambda kv: kv[1]))
