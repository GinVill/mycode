#!/usr/bin/env python3

""" Alta3 Research - Exploring Open APIs with requests """

import requests
import pprint

AOIF_CHAR = 'https://www.anapioficeandfire.com/api/characters/'

def main():
    #Request user input
    got_charToLookup = input('Pick a number between 1 and 1000 to return infor on a GoT character: ')

    #Send GET request to API url
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    #Decode the JSON returned and use Pretty Print to make it legible
    got_dj = gotresp.json()
    pprint.pprint(got_dj)
    
    allegiances = got_dj['allegiances']['name']
    print(allegiances)

    books = got_dj['books']['name']
    print(books)


if __name__ == '__main__':
    main()

