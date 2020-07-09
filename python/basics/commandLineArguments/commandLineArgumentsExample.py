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

