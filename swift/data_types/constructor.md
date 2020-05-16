# Building a constructor

```swift
struct User {

    let username: String
    let firstName: String
    let lastName: String
    let email: String
    let password: String
    let birthDate: Date

    init(username: String, firstName: String, lastName: String, email: String, password: String, birthDate: Date) {

        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.birthDate = birthDate

    }

}
```
