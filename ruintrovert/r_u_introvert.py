#!/usr/bin/env python3

score = 0

answer = input("Do you get nervous before phone calls?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1
answer = input("Do you sweat before turning your camera on?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1
answer = input("Do you like Covid restrictions?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1
answer = input("Do you feel like television or game characters are your friends?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1
answer = input("Are delivery drivers your most frequent guests?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1
answer = input("Do you feel relieved when someone else cancels plans?: y or n ").strip(" ").lower()
if answer == "y":
    score += 1

if score >= 5:
    print("Perhaps people don't like you either.")
elif score >= 3 and score <5:
    print("Be sure to take your vitamin D supplements in lieu of daylight.")
elif score >= 1 and score < 3:
    print("Not yet, young Jedi...")
else:
    print("WHAT makes you think you are an introvert?")
