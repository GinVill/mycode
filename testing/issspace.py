#!/usr/bin/python3
"""Alta3 Research | Script to interact with Astros API"""

import requests

def astros():
    r = requests.get("http://api.open-notify.org/astros.json")
    if r.status_code == 200:
        return r.json()
    else:
        return None
    
def main():
    print("Right now in space we have...")
    print(astros())

# This statement becomes critical if we are going to import our code into a test suite.
# Without it, main() would auto-execute when it was imported into the test suite.
if __name__ == "__main__":
    main()

