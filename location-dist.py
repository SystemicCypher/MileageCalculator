import os
from selenium import webdriver

def urlify(str):
    return str.replace(',','').replace(' ','+')

home = 'street+addr+separated+by+pluses+city+st'
maps = 'https://google.com/maps/dir'

loc = open("locations.txt", 'r')
miles = open("mileage.txt", 'w')

#driver = webdriver.Chrome()

lines = loc.readlines()

url = ''
for i in range(len(lines)):
    if '-' in lines[i]:
        url += '/' + home + '/'
        continue

    url += urlify(lines[i])
    url += '/'
    
    if i+1 < len(lines) and '-' in lines[i+1]:
        print(maps+url+home+'/')
        #driver.get(maps+url+home+'/')
        break

