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

## Saving and Restoring the Table's Current State
 

