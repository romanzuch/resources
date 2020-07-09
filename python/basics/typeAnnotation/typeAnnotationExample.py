#!/usr/bin/python python3
import typing

def first() -> None:
	print("This function does not return anything")

def second(message: str) -> str:
	return "This function returns a message as string " + message

first()
second("Hello World!")
