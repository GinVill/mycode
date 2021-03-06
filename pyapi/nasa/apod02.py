#!/usr/bin/env python3

import requests

NASAAPI = 'https://api.nasa.gov/planetary/apod?'

def main():
    # Get credentials from separate file
    with open('/home/student/nasa.creds', 'r') as mycreds:
        nasacreds = mycreds.read()
    # remove any newline characters from the api_key
    nasacreds = 'api_key=' + nasacreds.strip('\n')

    # make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    #  strip off json
    apod = apodresp.json()

    print(apod)

    print()
    
    print(apod['title'] + '\n')

    print(apod['date'] + '\n')

    print(apod['explanation'])

    print(apod['url'])

    # In the range specified, which is the largest asteroid?
    dates =[]
    # loop across each key in near_earth_objects
    for dictionary in apod['near_earth_object']:
        print(dictionary.keys())
    print(apod)

if __name__ == '__main__':
    main()
