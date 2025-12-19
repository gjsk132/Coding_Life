input = open(0).readline

before_vowels = "aiyeou"
before_consonants = "bkxznhdcwgpvjqtsrlmf"

resolve_rules = {}

for before, after in zip(before_vowels, before_vowels[3:]+before_vowels[:3]):
    resolve_rules[before] = after
    resolve_rules[before.upper()] = after.upper()

for before, after in zip(before_consonants, before_consonants[10:]+before_consonants[:10]):
    resolve_rules[before] = after
    resolve_rules[before.upper()] = after.upper()

while True:
    line = input()

    if not line:
        break

    for ch in line:
        if ch in resolve_rules:
            print(resolve_rules[ch], end="")
        else:
            print(ch, end="")