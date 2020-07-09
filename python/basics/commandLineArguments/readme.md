# Command Line Arguments

## What are Command Line Arguments

A command line argument is an extra command you can use when launching a program. By doing so you can change the program's behaviour. 
For more basic information please refer to this [page](https://www.bleepingcomputer.com/tutorials/understanding-command-line-arguments-and-how-to-use-them/)

## How to use in Python

Python provides different approaches to implement command line arguments in your script. The Python `sys` module provides access to any command line arguments via the `sys.argv`.

```python
import sys
```

### Parsing Command Line Arguments

Python provides a `getopt` module that helps you parse command line arguments and options. This module provides two functions and an exception to enable parsing.

#### getopt.getopt method

```python
getopt.getopt(args, options, [long_options])
```

- args &rarr; argument list to be parsed
- options &rarr; string of options letters that the script wants to recognize, with options that require an argument should be followed by a colon (:)
- long_options &rarr; optional parameter and if specified, must be a list of strings with the names of the long options, which should be supported
- returns value consiting of two elements: (1) list of option/value pairs, (2) list of program arguments left after the option list was stripped

## Example

```python
#!/usr/bin/python python3

import sys, getopt, typing

def main(argv) -> str:
	input = ""
	output = ""
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
	except getopt.GetoptError:
		print("commandLineArguments.py -i <inputfile> -o <outputfile>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			print("commandLineArguments.py -i <inputfile> -o <outputfile>")
			sys.exit()
		elif opt in ("-i", "--input"):
			input = arg
		elif opt in ("-o", "--output"):
			output = arg
	print("Input is ", input)
	print("Output is ", output)

if __name__ == "__main__":
	main(sys.argv[1:])
```

