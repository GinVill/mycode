#!/usr/bin/env python3

""" Alta3 research - Exploring Open APIs with requests """

import requests

AOIF_BOOKS = 'https://www.anapioficeandfire.com/api/books'

def main():
    # Send the get request to the API url
    gotresp = requests.get(AOIF_BOOKS)

    # Decode the JSON returned
    got_dj = gotresp.json()

    # Iterate over response
    for singlebook in got_dj:
        # Display the names of each book - ALL below statements do the same thing
        print(singlebook['name'] + ',', 'pages -', singlebook['numberOfPages'])
        print('{}, pages - {}'.format(singlebook['name'], singlebook['numberOfPages']))
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")

        # Print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

if __name__ == '__main__':
    main()

