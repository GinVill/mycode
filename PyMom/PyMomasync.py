#!/usr/bin/env python3

import wolframalpha  #necessary for answers
client = wolframalpha.Client('A4223Y-632JHKW8W4')

import PySimpleGUI as sg  #necessary for popup windows
# You have to install as follows on command line:
# pip install pysimplegui
# or: pip3 install pysimplegui

import asyncio
import time
import random
import datetime as dt

otherHostPath = 'etc/hosts' # This is for a linux or mac host machine
windowsHostPath =r'C:\Windows\System32\drivers\etc\hosts' # This is for a windows host machine
localRedirect = '127.0.0.1' # Local address variable
startTime = 7 # set block start time variable
endTime = 18 # set block end time variable
blockStart = dt.time(startTime) #define formatted start time
blockEnd = dt.time(endTime)  # define formatted end time

# List of websites blocked during working hours
sitesBlocked = ['facebook.com', 'www.facebook.com', 'instagram.com', 'www.instagram.com', 'twitter.com', 'www.twitter.com', 'youtube.com', 'www.youtube.com']

def nagWindow():
    sg.theme('dark teal 6')  # Establish window color theme
    # Define the window's contents
    layout = [[sg.Text("Enter a question, then click OK")],  # instruction to user
              [sg.InputText()],  # input capture
              [sg.Text(size=(40, 1), key='-OUTPUT-')],
              [sg.Button('Ok'), sg.Button('Block'), sg.Button('Reminder'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('PyMom - the nag you need', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':

            break
        elif event == 'Block':
            sg.Popup(sitesBlocked, title='These sites are blocked.')
        elif event == 'Ok':
            try:
                response = client.query(values[0])
                # Output a message to the window
                sg.Popup(next(response.results).text)
            except:
                print('Sorry, kid. Try google.')

    # Finish up by removing from the screen
    window.close()


def helpfulNags():
    helperNags = ["Remember to take a break. Do some planks.",
                  "Make sure to drink some water. It's good for you.",
                   "Take a walk today. Exercise helps your brain.",
                   "If you are tired of working, you can always clean your room.",
                   "Did you feed the dog? Sugar Cupcake gets crazy if we skip her meal.",
                   "Take 10 and do some push-ups, then drink some water.",
                   "Be sure to tidy up. Brains think better with less distraction.",
                   "Please check Sugar Cupcake's water. And have some yourself.",
                   "Little breaks help. Do some crunches and some burpees.",
                   "Maybe it's time for a snack? Make a healthy choice"]

    sg.Popup(random.choice(helperNags))
    time.sleep(180)

def webBlocker():
    # TODO: Change this forever loop when integrating all functions
    while True:  # Start a FOREVER LOOP
        time.sleep(900)  # to check the time every 15 minutes
        if (blockStart) <= dt.datetime.now().time() and dt.datetime.now().time() <= (
        blockEnd):  # and see if it is working hours
            print("You are SUPPOSED to be working....")  # the NAG
            with open(windowsHostPath, 'r+') as file:  # open the host file to read and write
                fileContent = file.read()  # and read the content into fileContent
                for website in sitesBlocked:  # search for text from sitesBlocked list
                    if website in fileContent:  # if it is already there,
                        pass  # skip this process
                    else:  # otherwise
                        file.write(
                            localRedirect + '  ' + website + '\n')  # add new line with localRedirect and website name
        else:  # otherwise, if it is NOT working hours
            print("You are free to waste time....")  # the NAG
            with open(windowsHostPath, 'r+') as file:  # open the host file to read and write
                fileContent = file.readlines()  # and read the content by line into fileContent\
                file.seek(0)  # starting at the beginning
                for line in fileContent:  # check each line
                    for website in sitesBlocked:  # for sitesBlocked list values
                        if website not in fileContent:  # if the website is NOT in that line
                            file.write(line)  # write the line, as is
                        file.truncate()  # otherwise, stop the writing here, meaning don't write anymore, which won't include web blocks

def reminders():
    print("reminders")


def main():
    webBlocker()

    loop = asyncio.get_event_loop() # Connect, or create, event loop
    loop.call_soon(nagWindow) #Schedule the first function to run
    loop.call_soon(helpfulNags)
    loop.run_until_complete(asyncio.sleep(1))



if __name__ == '__main__':
    main()