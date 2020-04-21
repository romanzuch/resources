# UITableView
> A view that presents data using rows arranged in a single column.

## Overview
- table views display a single column of vertically scrolling content, divided into rows
- UITableView manages the basic appearance of the table; the app provides the cells (UITableViewCells) that display the actual content
- standard cell configurations display a simple combination of text and images
- custom cells that display any content can be configured
- header and footer views can provide additional information for groups of cells

<img src="https://docs-assets.developer.apple.com/published/722508d93c/1eb44f8d-1907-4949-9208-f2fb7f3ffd1b.png">

## Adding a Table View to Your Interface
- to add a table view to your interface, drag a Table View Controller (UITableViewController) object to your storyboard
- XCode creates a new scene that includes both the view controller and a table view
- table views are data driven, normaly getting data from a data source object that you provide
- the data source object manages your app's data and is responsible for creating and configuring the table's cells
- specify your table's data, see [Filling a Table with Data](https://developer.apple.com/documentation/uikit/views_and_controls/table_views/filling_a_table_with_data)

### Filling a Table with Data
> Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.

**Overview**
- use a data source object to provide data for the table view
- a data source object adopts the `UITableViewDataSource` protocol

**Provide the Numbers of Rows and Sections**
- before appearing on screen, a table view asks you to specify the total numbers of rows and sections
- the data source object provides this information using two methods:
```swift
func numberOfSections(in: UITableView) -> Int // Optional

func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int 
``` 
- return the row and section counts as quickly as possible 
- doing so might require you to structure your data in a way that makes it easy to retrieve the row and section information
- the example code below show an implementation of the data source methods that return the number of rows and sections in a *multisection table*

```swift
var hierarchicalData = [[String]]()

override func numberOfSections(in tableView: UITableView) -> Int {
	return hierarchicalData.count
}

override func tableView(_ tableView: UITableView,
			numberOfRowsInSection section: Int) -> Int {
	return hierarchicalData[section].count
}
```

**Define the Appearance of Rows**
- you define the appearance of your table's rows in your storyboard file using cells
- a cell is a `UITableViewCell` object that acts like a template for the rows of your table
- cells are views, and they contain any subviews that you need to display your content
- labels, image views, and other views can be added to their content area 
- to add more prototype cells to a table view, select the table view and update its Prototype Cells attribute
- when creating a cell with a custom view, define a subclass of `UITableViewCell` to manage those views >> in your subclass, add outlets for the custom view that display your app's data, and connect those outlets to the actual views >> configure the cell at runtime


**Create and Configure Cells for Each Row**
- before a table appears onscreen, it asks its data source object to provide cells for the rows
- your data source object's `tableView(_:cellForRowAt:)` method must respond quickly
- implement this method with the following pattern:
	- call the table view's `dequeueReusableCell(withIdentifier:for:) method 
	- configure the cell's views with your app's custom data
	- return the cell to the table view
- for standard cell styles, `UITableViewCell` contains properties with the views you need to configure >> for custom cells, you add views to your cell at design time and outlets to access them
- the example code shows a version of the data source method that configures a cell containing a single text label:

```swift
override func tableView(_ tableView: UITableView, 
			cellForRowAt indexPath: IndexPath) -> UITableViewCell {
	// Ask for a cell of the appropriate type.
	let cell = tableView.dequeueReusableCell(withIdentifier: "basicStyleCell", for: indexPath)

	// Configure the cell's contents with the row and section number.
	// The Basic cell style guarantees the label view is present in textLabel.
	cell.textLabel!.text = "Row \(indexPath.row)"
	return cell
}
```

- table views do not ask you to create cells for each of the table's rows
- creating cells lazily reduces the amount of memory the table uses
- however, it also means your data source object must create cells quickly
- do not use `tableView(_:cellForRowAt:)` method to load your table's data or perform lengthy operations

**Prefetch Data to Improve Performance**
- scrolling performance for table views is critical
- if fetching the data for your table involves an expensive operation, such as fetching it from a database, use a prefetching data source object >> an object, that adopts the `UITableViewDataSourcePrefetching` protocol >> begin loading the data asynchronously before it scrolls into view

**Specify Data Statically in the Storyboard**
- 





## Saving and Restoring the Table's Current State
 

