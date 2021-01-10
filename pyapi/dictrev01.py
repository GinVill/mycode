#!/use/bin/env python3

def main():
    hostIPDict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    # Display the current state of our dictionary
    print(hostIPDict)

    #add another entry to the dictionary
    hostIPDict['host04'] = '10.23.43.224'

    # display the revised dictionary
    print(hostIPDict)

    # change the value for host02
    hostIPDict['host02'] = '192.168.70.55'

    # display the revised dictionary again
    print(hostIPDict)
    # and display the new value for host02
    print(hostIPDict['host02'])

if __name__ == '__main__':
    main()

