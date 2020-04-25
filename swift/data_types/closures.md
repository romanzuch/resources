# Closures in Swift

## Functions as Data
Swift picks up the idea from functional programming. Closures make functions seamlessly integrated into Swift's types and therefore functions can be used *like data*. 

```swift
func power(value: Int) -> Int {
    return pow(value, 2)
}
```
```swift
let operation = power
operation(10) // returns 100
```
```swift
func process(value: Int, operation: (Int) -> (Int)) -> Int {
    return operation(value)
}
```
 For example, a reference to a function can be stored in a variable or passed as a parameter. The parameter types and return values must be declared.
 With `(Int) -> (Int)`, you declare that a function must be passed that receives an `Int` value as parameter and returns an `Int` value.

 ## Closures
The principle of functions as data is extended by closures. A *closure* is a anonymously defined function.
```swift
let operation = { (value: Int) -> (Int) in
    return pow(value, 2)
}
operation(10) // returns 100
```

The function/closure is able to access its creation context. By using values declared in the context - not in the closure/function itself - they are bound to the closure. Binding the required values to the closure is called *capture*.

```swift
let multiplier = 5
let operation = { (value: Int) -> (Int) in
    return pow(value, multiplier)
}
operation(10) // returns 100000
```

## Some more example code

```swift
let names = [James, Adam, Andrew, William]

names.filter { (value: String) -> Bool in
    return value.count < 6 // returns [James, Andrew, William]
}
```