from collections import deque
vowels = deque(list(map(str, input().split(" "))))
consonants = deque(list(map(str, input().split(" "))))
rose = ['r', 'o', 's', 'e']
tulip = ['t', 'u', 'l', 'i', 'p']
lotus = ['l', 'o', 't', 'u', 's']
daffodil = ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']
word_found = False

while vowels and consonants:
    if vowels[0] in rose:
        while vowels[0] in rose:
            rose.remove(vowels[0])

    if vowels[0] in tulip:
        while vowels[0] in tulip:
            tulip.remove(vowels[0])

    if vowels[0] in lotus:
        while vowels[0] in lotus:
            lotus.remove(vowels[0])

    if vowels[0] in daffodil:
        while vowels[0] in daffodil:
            daffodil.remove(vowels[0])

    if consonants[-1] in rose:
        while consonants[-1] in rose:
            rose.remove(consonants[-1])

    if consonants[-1] in tulip:
        while consonants[-1] in tulip:
            tulip.remove(consonants[-1])

    if consonants[-1] in lotus:
        while consonants[-1] in lotus:
            lotus.remove(consonants[-1])

    if consonants[-1] in daffodil:
        while consonants[-1] in daffodil:
            daffodil.remove(consonants[-1])

    vowels.popleft()
    consonants.pop()
    if len(rose) == 0 or len(tulip) == 0 or len(lotus) == 0 or len(daffodil) == 0:
        word_found = True
        break

if word_found == True:
    if len(rose) == 0:
        print(f"Word found: rose")
    elif len(tulip) == 0:
        print(f"Word found: tulip")
    elif len(lotus) == 0:
        print(f"Word found: lotus")
    elif len(daffodil) == 0:
        print(f"Word found: daffodil")

else:
    print("Cannot find any word!")

if len(vowels) > 0:
    print(f"Vowels left: {' '.join(vowels)}")
if len(consonants) > 0:
    print(f"Consonants left: {' '.join(consonants)}")