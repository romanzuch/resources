# UICollectionViewController

## Declaration

```swift
class UICollectionViewController: UIViewController
```

If you create the collection view controller programmatically, it automatically creates a new unconfigured collection view object, which you can access using the `collectionView` property. If the collection view controller has an assigned nib file or was loaded from a storyboard, it loads its view from the corresponding. When the collection view is about to appear for the first time, the collection view controller reloads the collection view data. It also clears the current selection every time the view is displayed. This behaviour can be changed by setting the value of `clearsSelectionOnViewWillAppear` to `false`.

When you initialize a collection view controller, using `init(collectionViewLayout:)`, you specify the layout the view should have. Because the initially created view is without any dimensions or content, the view's *data source* and *delegate* (*typically the collection view controller itself*) must provide this information.

For each view you want to manage, you create a custom subclass of `UICollectionViewController`. You may override the `loadView()` method or any other *superclass* method, but be sure to call *super* in the implementation of your method.

## Further topics
### Initializing the UICollectionViewController Object

```swift
init(collectionViewLayout: UICollectionViewLayout)
```
*Initializes a collection view controller and configures the collection view with the provided layout.*

### Getting the Collection View

```swift
var collectionView: UICollectionView!
```
*The collection view object managed by this view controller*

```swift
var collectionViewLayout: UICollectionViewLayout
```
*The layout object used to initialize the collection view controller*

### Configuring the Collection View Behavior

```swift
var clearsSelectionOnViewWillAppear: Bool
```
*A Boolean value indicating if the controller clears the selection when the collection view appears*

```swift
var installsStandardGestureForInteractiveMovement: Bool
```
*A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process*

### Integrating with a Navigation Controller

```swift
var useLayoutToLayoutNavigationTransitions: Bool
```
*A Boolean that indicates whether the collection view controller coordinates with a navigation controller for transitions*
