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

## The setter method – When to use it and How to write one?

## The deleter method
