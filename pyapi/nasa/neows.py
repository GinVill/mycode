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
    #Create a list of dates
    dates = []
    for x in neodata['near_earth_objects']:
        dates.append(x)
    print(dates)

    for x in dates:
        for asteroidInDict in neodata['near_earth_objects'][x]:
            asteroidInDict['estimated_diameter']['miles']['estimated_diameter_max']
    
    """In the range specified, which is the largest asteroid?
        In the range specified, how many asteroids are labeled "Potentially Hazardous"
        What are the names of these 'fatal' asteroids? """

if __name__ == '__main__':
    main()

