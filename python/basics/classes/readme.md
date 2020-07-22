# Python Classes

[Link](https://www.machinelearningplus.com/python/python-property/)

## What does @property do?
- the `@property` is used to let a method to be accessed as an attribute instead of as a method 

## When to use @property?
- by adding `@property` decorator before a method, you can access it as an attribute instead of with a `()`
- this can avoid problems with the code
```python
 @property    
    def fullname(self):
        return self.first + ' '+ self.last
```
```python
# Init a Person 
person = Person('selva', 'prabhakaran')
print(person.fullname)  #> selva prabhakaran

# Change last name to Prasanna
person.last = 'prasanna'

# Print fullname
print(person.fullname)  # selva prasanna
```

## The setter method – When to use it and How to write one?
- now you are able to access a method like an attribute
- however there is still a problem
- at this stage, trying to change `fullname` will throw an `AttributeError`
- here you have to set a `setter` method that will be called, everytime a user sets a value to this property
- inside the setter method you can change the values of variables
- the setter method should have the same name as the `@property` decorated method
- it accepts as argument the value that a user sets to the property

```python
@property
def fullname(self):
	return self.first + " " + self.last

@fullname.setter
def fullname(self, name):
	firstname, lastname = name.split()
	self.first = firstname
	self.last = lastname
```

## The deleter method
- the deleter method defines what happens when a property is deleted
```python
@fullname.delter
def fullname(self):
	self.first = None
	self.last = None
```
```python
del person.fullname
``` 

