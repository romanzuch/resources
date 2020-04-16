# UIViewController

**Declaration**

```swift
class UIViewController : UIResponder
```

**Main responsibilities**
- *update* the contents of the view, usually in response the *changes to the underlying data*
- responding to *user interactions*
- *resizing* views
- *managing* the layout of the overall interface
- *coordinating* with other objects in an app

**Notes**
- view controllers are *UIResponder* objects
- inserted into the *responder chain* between view controller's root view and that view's superview (typically belongs to another view controller)
- you often use multiple view controllers, each owning a portion of the app's user interface
```markdown
For example, one view controller might display a table of items while a different view 
controller displays the selected item from that table.
```
