#!/usr/bin/env python3

def main():
    # a list of Alta3 classes
    alta3Classes = ['python_basics', 'python_api_design', 'python_for_networking', 'kubernetes', \
            'sip', 'ims', '5g', '4g', 'avaya', 'ansible', 'python_and_ansible_for_network_automation']

    #display the list
    print(alta3Classes)

    #use the len() function to determine the length
    print(len(alta3Classes))

    #display python_basics
    print(alta3Classes[0])

    #display SIP
    print(alta3Classes[4])

    #display andsible
    print(alta3Classes[9])

    print(alta3Classes[0:3])

    print(alta3Classes[2:5])

    print(alta3Classes[-1])

if __name__ == '__main__':
    main()

