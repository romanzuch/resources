# Capture Lists in Swift: Difference between weak, strong, and unowned.
[https://www.hackingwithswift.com/articles/179/capture-lists-in-swift-whats-the-difference-between-weak-strong-and-unowned-references](https://www.hackingwithswift.com/articles/179/capture-lists-in-swift-whats-the-difference-between-weak-strong-and-unowned-references)

## What is a Capture List?
A capture list comes before a closure's parameter. Capture lists capture values from the environment as either strong, weak, or unowned. It is used a lot to avoid strong reference cycles.

## What is a Closure?
> Closures are self-contained blocks of functionality that can be passed around and used in your code. Closures in Swift are similar to blocks in C and Objective-C and to lambdas in other programming languages.
Closures can capture and store references to any constants and variables from the context in which they are defined. This is known as closing over those constants and variables. Swift handles all of the memory management of capturing for you.

```swift
var number = 0

let increment: () -> () = {
    number += 1
    print(number)
}
```

## What is a Reference Cycle?
- a closure referes back to a object, that holds the closure
    - an object has a stored property that refers to a closure
    - that closure refers back to `self` 

```swift
class Increment {
    var number = 0

    lazy var incrementNumber: (Int) -> () = { value in
        self.number += value
        print(self.number)    
    }
}

let increment = Increment()
increment.incrementNumber(3)
```

The above example can cause a memory leak. The closure refers back to the object itself, it refers to self in order to increment the number, and that will create a reference cycle.

**Let's fix this**
By refering to self as a weak property `[ weak self ]` there won't be a strong reference. 

```swift
lazy var incrementNumber: (Int) -> () = { [ weak self ] value in
        self.number += value
        print(self.number)
```

## Weak vs strong vs unowned – know the difference in closures

Let's take a look at our problem.

```swift
class Singer {
    func playSong() {
        print("Shake it off!")
    }
}
```

Now we create a function that (1) creates an instance of `Singer`, (2) creates a closure that uses the singer's `playSong()` method, and (3) returns that closure for us to use elsewhere.

```swift
func sing() -> () -> Void {
    let taylor = Singer()

    let singing = {
        taylor.playSong()
        return
    }

    return singing
}
``` 

Finally, we can call `sing()` to get back a function we can use whereever we want to have `playSong()` printed.

```swift
let singFunction = sing()
singFunction()
```

### Strong Capturing
Swift uses strong capturing by default. A closure will capture any external values that are used inside it. Swift makes sure these values will never get destroyed. 
Looking at the function above, the `taylor` constant is made inside the `sing()` method, so it would be destroyed when the function ends. Strong capturing means, that the constant will stay *alive* as long as the closure exists. If Swift allows `taylor` to be destroyed, the closure wouldn't be safe to call. `taylor.playSong()` wouldn't be valid anymore. 

### Weak Capturing
Most commonly used as alternative to *strong capturing* is *weak capturing*. You can specify in the *capture list* how values used inside the closure should be captured. How does *weak capturing* changes the way values are captured:
    1. Weakly captured values aren't kept alive by the closure. They are set to `nil` after the function ends.
    2. Weakly captured values are **always** optional, as a result of 1. 

```swift
func sing() -> () -> Void {
    let taylor = Singer()

    let singing = { [ weak taylor ]
        taylor?.playSong()
        return
    }

    return singing

}
```

`[ weak taylor]` is the capture list. We treat `taylor` as a weak value, therefor it is optional. This code won't print anything anymore, because the closure inside `sing()` doesn't keep a strong hold of `taylor`.

### Unowned Capturing
Unowned capturing behaves more like implicitly unwrapped optionals. It allows values to become `nil` at any point in the future. However, you can work with them as **if** they are always going to be there. No need of unwrapping optionals.
