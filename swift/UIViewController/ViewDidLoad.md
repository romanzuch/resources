# viewDidLoad() 

> Called after the controller's view is loaded into memory.

**Declaration**
```swift
func viewDidLoad()
```

**Discussion**
- method is called after the vc has loaded its view hierarchy into memory
- you usually override this method to perform additional initialization on views

**Managing the View**
- [`var view: UIView!`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view)
- [`var viewIfLoaded(): UIView?`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621360-viewifloaded)
- [`var isViewLoaded(): Bool`](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097563-isviewloaded)
- [`func loadView()`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview)
- [`func loadViewIfNeeded()`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621446-loadviewifneeded)
- [`var title: String?`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title)
- [`var prefferedContentSize: CGSize`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621476-preferredcontentsize)

