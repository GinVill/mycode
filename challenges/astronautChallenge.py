#!/usr/bin/env python3
"""Author: Gina Villegas
To provide facts about astronauts at Space Station
"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json").json()

    print("People in space: ", r["number"])

    for astro in r["people"]:
        print(f"{astro['name']} on the {astro['craft']}")
main()

