#!/usr/bin/env python3

import requests

# Define NEOW URL
NEOURL = 'https://api.nasa.gov/neo/rest/v1/feed?'

def main():
    # First, access credentials in a separate file
    with open('/home/student/nasa.creds', 'r') as mycreds:
        nasacreds = mycreds.read()
    # Remove any newline characters from the API key
    nasacreds = 'api_key=' + nasacreds.strip('\n')

    # Establish the date we want to search
    startdate = 'start_date=2019-11-11'

    # This value is not being used in this version
    # enddate = 'end_date=END_DATE'

    # send request to URL with relevant information and credentials
    neowrequest = requests.get(NEOURL + startdate + '&' + nasacreds)

    # decode the JSON object returned
    neodata = neowrequest.json()

    # display NASA's NEOW data
    print(neodata)

if __name__ == '__main__':
    main()

