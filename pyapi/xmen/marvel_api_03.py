#!/usr/bin/env python3
import argparse
import time
import requests
import hashlib

## Define the API here - this is the URL we request from
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
## Generates a timestamp(timeywimey, private key & public key hash
## As required per Marvel API
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
## Sends the actual request to Marvel, using the 
## API(XAVIER,character, timestamp, public key and hash
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    ## Then prints all that to the screen
    print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    ## And returns the JSON that Marvel returned
    return r.json()

    
def main():           
    
    ## harvest private key - reads and sanitizes private key from separate file
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')
    
    ## harvest public key - reads and sanitizes public key from separate file
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')
    
    ## create an integer from a float timestamp (for our RAND)
    nightcrawler = str(time.time()).rstrip('.')
    
    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, args.hero)
    
    ## display results
    print(uncannyxmen['name'])

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv \
      containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub \
      containing Marvel public developer key')
    
    ## The line below is NEW! This allows us to pass the lookup character
    parser.add_argument('--hero', \
      help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()

