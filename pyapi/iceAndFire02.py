#!/use/bin/env python3

""" Alta3 Research - Exploring Open APIs with requests """

import pprint
import requests

# Set the URL to a variable for code ease
AOIF_BOOKS = 'https://www.anapioficeandfire.com/api/books'

def main():
    # Send GET request to API url
    gotresp = requests.get(AOIF_BOOKS)

    # Decode the JSON response
    got_dj = gotresp.json()

    # Print the response using Pretty Print to make it legible
    pprint.pprint(got_dj)

if __name__ == '__main__':
    main()

