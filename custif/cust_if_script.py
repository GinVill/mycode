#!/usr/bin/env python3

score = 0
index = 0

questions = ["Do you get nervous before phone calls?", "Do you sweat before turning your camera on?", "Do you enjoy Covid restrictions?", "Do you feel like television or game characters are your friends?", "Are delivery drivers your most frequent guests?", "Do you feel relieved when someone else cancels plans?"]

print("Let's determine whether you might be an introvert!")
print("Please enter y for yes and n for no")
print("Enter q at anytime to quit")

while index < len(questions):
    try:
        answer = input(questions[index]).strip().lower()
        if answer == "q":
            print("Thanks for playing. Goodbye")
            break
        elif answer == "y":
            score += 1
            index += 1
        elif answer == "n":
            index +=1
    except:
        print("Please enter a valid answer. y  n  or q")


if score >= 5:
    print("You are an introvert but perhaps people don't like you either.")
elif score >= 3 and score <5:
   print("You are pretty close to introvert status so be sure to take your vitamin D supplements in lieu of daylight.")
elif score >= 1 and score < 3:
   print("Not yet, young Jedi...")
else:
   print("Not an introvert, but maybe not the funnest extrovert?")
