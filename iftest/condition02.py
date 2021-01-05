#!/usr/bin/env python3
## sets variable hostname to user input
hostname = input("What value should we set for hostname?")
## if the hostname is true (= mtg) it will print
## we set the input to .lower to standardize the input
if hostname == "mtg":
    print("hostname matches expected config")

elif hostname.lower() == "mtg":
    print("The hostname was found to be mtg")

print("Exiting the script.")
