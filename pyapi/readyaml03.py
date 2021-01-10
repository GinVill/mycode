#!/usr/bin/env python3

# if not already installed, on the command line use:
#python3 -m pip install pyyaml
import yaml

def main():
    #open some yaml data
    with open('myYAML.yml', 'r') as yf:
        #convert YAML file to python data structures (lists and dictionaries)
        pyyammy = yaml.load(yf)
    #display our new Python data
    print(pyyammy)

if __name__ == '__main__':
    main()

