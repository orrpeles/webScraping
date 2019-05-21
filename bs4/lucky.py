#!/bin/python
# lucky.py - opens 5 first search results on google search

import sys, bs4, requests, webbrowser

print('googling...') #display text while downloading google search results
res = requests.get('https://www.google.com/search?q=' + " ".join(sys.argv[1:])) #user will specify search term on command line
res.raise_for_status()

#Retreive top search results
soup = bs4.BeautifulSoup(res.text, features='lxml') # later argument omits an irrelevant warning message about the OS

#Open browser tab for each result
linkElems = soup.select('.r a')
# this is a better way of searching for classes on bs4: https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
numOpen = min(5, len(linkElems)) #open minimum 5 first results or the amount that linkElems passes, the minimum of the two
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href')) #get('href') gets the search results that procedes google.com 

# small bug found that this program doesn't print out cached results, there could be inconsistencies between displayed results on google and the one in this program when under a proxy or when visiting different country


    





