#!/usr/bin/env python3

#if not already installed, on command line use:
#python3 -m pip install pyyaml
import yaml

def main():
    #open YAML data
    with open('myYAML.yml', 'r') as myf:
        #pull in YAML as Python lists and dictionaries
        pyyammy = yaml.load(myf)
    #check out the data
    print(pyyammy)
    #add Minecraft to the list of apps
    pyyammy[0]['apps'].append('minecraft')
    #did the data change?
    print(pyyammy)
    #open a file to dump to
    with open('myYAML.yml.updated', 'w') as myf:
        #use the YAML library yaml.dump(input data, file-like object)
        yaml.dump(pyyammy, myf)

if __name__ == '__main__':
    main()
