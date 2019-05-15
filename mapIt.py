#!/bin/python
# mapIt.py - launches map in browser using cmd line or clipboard

import webbrowser, sys, pyperclip
if len (sys.argv) > 1: # if I type in cmd line anything after 'python mapIt.py'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

#print(address)
