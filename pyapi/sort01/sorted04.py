#!/usr/bin/env python3

simpsons = [('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34)]

def byAge(characterbio):
    # isinstance can test if a value is an int, float, str, etc.
    if isinstance(characterbio[1], int):
        return characterbio[1]
    else:
        return 99  # if a user does not have an age, return 1000
        # which will put them at the end of the list

simpsonsAge = sorted(simpsons, key=byAge)

print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)

