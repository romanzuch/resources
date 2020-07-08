#!/usr/bin/python python3 

import re

# import the given text
searchableText = open(example_text.txt)

# define patter to search for Lorem in given text
searchPattern = re.compile("lorem")

# iterate through the lines of the text 
findings: Int = 0
for line in searchableText:
  if searchPattern.fullmatch(line.lower()):
    findings += 1

print("Found: {}".format(findings))
  
