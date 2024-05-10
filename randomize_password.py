word = "South Cleric, Arizona"

# All lowercase
print(word.lower())

# All uppercase
print(word.upper())

# Capitalize first letter of each word
print(word.title())

# Random capitalization
import random

def random_capitalization(word):
    result = ''
    for char in word:
        if random.choice([True, False]):
            result += char.upper()
        else:
            result += char.lower()
    return result

print(random_capitalization(word))

# Different spacing and comma variations including "southclericaz"
import itertools

def different_spacing(word):
    variations = []
    words = word.replace(',', '').split()
    for i in range(len(words)):
        for permutation in itertools.permutations(words, len(words) - i):
            variations.append(''.join(permutation))
    return variations

spacing_variations = different_spacing(word)
for variation in spacing_variations:
    print(variation)

# Adding "southclericaz" and similar variations
def add_similar_variations(variations, word):
    similar_variations = []
    similar_variations.append(word.replace(' Arizona', 'AZ').replace(' ', '').lower())
    similar_variations.append(word.replace(' Arizona', 'AZ').replace(' ', '').lower().replace(',', ''))
    similar_variations.append(word.replace(' Arizona', 'AZ').replace(' ', '').lower().replace(',', '').capitalize())
    variations.extend(similar_variations)

add_similar_variations(spacing_variations, word)

for variation in spacing_variations:
    print(variation)
