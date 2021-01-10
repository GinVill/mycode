#!/usr/bin/env python3

import json

def main():

    #create data to work with (a list of 2 dictionaries)
    hitchhikers = [{'name': 'Zaphod Beeblebrox', 'species':'Betelgeusian'}, {'name':'Arthur Dent', 'species':'human'}]

    #display the data
    print(hitchhikers)

    #open a new file in write mode
    with open('galaxyguide.json', 'w') as zfile:
        #use the json library - .dump(input data, file object)
        json.dump(hitchhikers, zfile)

if __name__ == '__main__':
    main()
    
