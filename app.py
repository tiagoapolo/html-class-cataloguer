#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
    print "No input - Use: python app.py <html-filepath>"
    exit()

inputFile = str(sys.argv[1])

try:
    with open(inputFile,'r') as html:
        output = open('output.txt','w+')
        for line in html:
            posInit = line.find("class=\"")
            if posInit >= 0:
                posEnd = line.find("\"", posInit+7) 
                txt = line[posInit+7:posEnd]       
                output.write(txt+"\n")

        html.close()
        output.close()
except IOError:
    print "File not found!"



