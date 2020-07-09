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

