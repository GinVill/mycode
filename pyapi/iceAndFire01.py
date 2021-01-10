#!/usr/bin/env python3

""" Alta3 Research - Exploring Open APIS with requests """
import requests

AOIF = 'https://www.anapioficeandfire.com/api'

def main():
    #Send HTTPS GET to the API of Ice and Fire
    gotresp = requests.get(AOIF)

    #Decode the response of JSON Object and set to variable
    got_dj = gotresp.json()

    #Use that variable to print the response
    print(got_dj)

if __name__ == '__main__':
    main()

