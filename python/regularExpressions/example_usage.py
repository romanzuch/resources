#!/usr/bin/python python3 

import re

# define patter to search for Lorem in given text
searchPattern = re.compile("lorem")

# iterate through the lines of the text 
findings: Int = 0
with open(example_text.txt) as searchableText:
  for line in searchableText:
    if searchPattern.fullmatch(line.lower()):
      findings += 1

print("Found: {}".format(findings))
  
