#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons

def main():
    """Runtime code. Always indent a function"""
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

# we must call our main function or our code will not run!
main()

