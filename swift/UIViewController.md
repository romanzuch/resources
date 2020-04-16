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

**Basics**
- view controllers are *UIResponder* objects
- inserted into the *responder chain* between view controller's root view and that view's superview (typically belongs to another view controller)
- you often use multiple view controllers, each owning a portion of the app's user interface
```markdown
For example, one view controller might display a table of items while a different view 
controller displays the selected item from that table.
```

## View Management
- each view controller manages a *view hierarchy* (the root view is stored in view property)
- the root view acts as a *container* for the rest of the view hierarchy
- several ways to specify the views for a view controller: 
  1. specify the view controller and its views in the *storyboard*; to load a view controller from a storyboard, call `instantiateViewController(withIdentifier:)`
  2. specify using a Nib file; a Nib file lets you specify the views of a single view controller, but doesn't let you define segues or relationships; create the vc programmatically and initialize using `init(nibName:bundle:)`
