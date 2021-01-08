#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget

def main():
    pokeChoice = input("What Pokemon character would you like to see?")
    
    try:
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokeChoice}").json()
        gameCount = len(pokeapi["game_indices"])
        print(f"{pokeChoice} has been in {gameCount} games.")        
        picURL = wget.download(pokeapi["sprites"]["front_default"])
        print(pokeapi["sprites"]["front_default"])
        #open(f"{pokeChoice}.txt", "wb").write(picURL.content)      
        for move in pokeapi["moves"]:
            pokeMoves = []
            pokeMoves.append(move['move']['name'])
            print(pokeMoves)            
        
    except:
        print("Please enter a valid Pokemon character.")
    
    
    
    
if __name__ == "__main__":
    main()
