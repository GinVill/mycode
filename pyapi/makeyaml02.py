#!/usr/bin/env python3

#YAML is not part of the standard library so we have to install it
# python3 -m pip install pyyaml
import yaml

def main():
    #create data to work with (a list of 2 dictionaries)
    hitchhikers = [{'name':'Zaphod Beeblebrox', 'species':'Betelgeusian'}, {'name':'Arthur Dent', 'species':'Human'}]

    #display the python data
    print(hitchhikers)

    #create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    #display the YAML string
    print(yamlstring)

if __name__ == '__main__':
    main()
