#!/usr/bin/env python3

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    #reading json from API by calling the API
    groundctrl = urllib.request.urlopen(MAJORTOM)

    #strip off JSON attachment and read it (as string)
    helmet =groundctrl.read()

    #display it as a string
    print(helmet)

    helmetson = json.loads(helmet.decode('utf-8'))

    #this type should say bytes
    print(type(helmet))

    #this type should say dictionary
    print(type(helmetson))

    print(helmetson['number'])

    #this returns a LIST of the people on this ISS
    print(helmetson['people'])

    #list the first astronaut in the list
    print(helmetson['people'][0])

    #list the second astronaut in the list
    print(helmetson['people'][1])

    #list the last astronaut in the list
    print(helmetson['people'][-1])

    #display every item in a list
    for astro in helmetson['people']:
        #display the value of astro
        print(astro)

    #for every time in a list
    for astro in helmetson['people']:
        #display ONLY the name value associated with astro
        print(astro['name'])

    #challenge - print number of people in space
    print('People in space: ', helmetson['number'])

    #challenge print name and craft of each person on ISS
    for astro in helmetson['people']:
        print(f'{astro["name"]} on the {astro["craft"]}')





if __name__ == '__main__':
    main()

