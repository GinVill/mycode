#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for value in farms[0]["agriculture"]:
        print (value)

farmNumber = input("""Want to see 
        1: NE farm, 
        2: W farm or 
        3: SE farm? 
        Please enter 1, 2 or 3""")
print(farms[farmNumber]["agriculture"]

animalsOnly = input("""Want to see animals only from 
1: NE Farm, 
2: W Farm or 
3: SE Farm? 
Enter 1, 2 or 3""")

if animalsOnly == 3:
    print(farms[animalsOnly][0]
else:
    print(farms[animalsOnly]["agriculture"]


