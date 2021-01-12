#!/usr/bin/env python3

us_invasion = [{'ip':'10.10.1.2', 'un':'john', 'pw':'allstar'}, \
{'ip':'10.10.1.3', 'un':'paul', 'pw':'iils20s3'}, \
{'ip':'10.10.1.4', 'un':'george', 'pw':'hunkydoryzory'}, \
{'ip':'10.10.1.5', 'un':'stuart', 'pw':'alta3'}, \
{'ip':'10.10.1.6', 'un':'pete', 'pw':'a8dd827z3'}]

def byUserName(x):
    return x['un']

def byIP(x):
    return x['ip']

def byPassword(x):
    return x['pw']

def byLastpass(x):
    return x['pw'][-1]

listbyusername = sorted(us_invasion, key=byUserName)

listByIPAddress = sorted(us_invasion, key=byIP)

listByPassword = sorted(us_invasion, key=byPassword)

listByLastpass = sorted(us_invasion, key=byLastpass)

print("\nThe list us_invasion looks like: ", us_invasion)

print("\nResult of sorted(us_invasion, key=byUserName): ", listbyusername)

print("\nBut the value of the list us_invasion hasn't actually changed: ", us_invasion)

print('\nThis list is sorted by IP address: ', listByIPAddress)

print('\nThis list is sorted by Password: ', listByPassword)

print('\nThis list is sorted by the last character in the Password: ', listByLastpass)

