#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginWin = 0 # counter for wins
loginFail = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line: # then we filter for only success
           loginFail += 1 # increment fail count
        elif "-] Authorization failed" in line: #which only has one dash
            loginWin += 1 # increment success count

print("The number of successful log in attempts is", loginWin)

