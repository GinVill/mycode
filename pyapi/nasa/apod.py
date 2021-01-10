#!usr/bin/env python3

import urllib.request
import json

#if you want to run in a GUI and open the URL in a browswer, uncomment the following
#import webbrowser

NASAAPI = 'https://api.nasa.gov/planetary/apod?'

def main():
    # define your credentials
    with open('/home/student/nasa.creds') as mycreds:
        nasacreds = mycreds.read()

    # remove any "extra" new line feeds on our key
    nasacreds = 'api_key=' + nasacreds.strip('\n')

    # call the webservice with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    # read the file-like objects
    apodread = apodurlobj.read()

    # decode returned JSON object to Python data structure
    apod = json.loads(apodread.decode('utf-8'))

    # display the Pythonic data
    print('\n\nConverted Python data')
    print(apod)

    print()

    print(apod['title'] + '\n')

    print(apod['date'] + '\n')

    print(apod['explanation'] + '\n')

    print(apod['url'])

    #uncomment the code below if you are using a GUI and want to open the URL
    #in a browser - use Firefox
    #input("\nPress Enter to open NASA Picture of Day in Firefox")
    #webbrowser.open(decodeapod['url'])
if __name__ == '__main__':
    main()

