#!/usr/bin/env python3

import json

def main():
    # create new data to work with
    hitchhikers = [{'name':'Zaphod Beeblebrox', 'species':'Betelgeusian'}, {'name': 'Arthur Dent', 'species':'Human'}]

    print(hitchhikers)

    jsonstring = json.dumps(hitchhikers)

    #display a single string of json
    print(jsonstring)

if __name__ == '__main__':
    main()

