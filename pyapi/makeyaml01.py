#!/usr/bin/env python3

#YAML is not part of the standard library
#so we had to install it (python3 -m pip install pyyaml)
import yaml

def main():
    #create data to work with
    hitchhikers = [{'name':'Zaphod Beeblebrox', 'species':'Betelgeusian'}, {'name':'Arthur Dent', 'species':'Human'}]

    #display data
    print(hitchhikers)

    #open a new file in write mode
    with open('galaxyguide.yaml', 'w') as zfile:
        # use YAML library yaml.dump(input data, file-like object)
        # unlike json, yamp uses .dump to create YAML strings and write to files
        #(json uses .dump() to create a strin and .dumps() to write to files)
        yaml.dump(hitchhikers, zfile)

if __name__ == '__main__':
    main()

