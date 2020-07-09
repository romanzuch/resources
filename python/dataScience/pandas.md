# [Pandas](https://github.com/pandas-dev/pandas)

## Main Features

- Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
- Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
- Automatic and explicit data alignment: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let Series, DataFrame, etc. automatically align the data for you in computations
- Powerful, flexible group by functionality to perform split-apply-combine operations on data sets, for both aggregating and transforming data
- Make it easy to convert ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects
- Intelligent label-based slicing, fancy indexing, and subsetting of large data sets
- Intuitive merging and joining data sets
- Flexible reshaping and pivoting of data sets
- Hierarchical labeling of axes (possible to have multiple labels per tick)
- Robust IO tools for loading data from flat files (CSV and delimited), Excel files, databases, and saving/loading data from the ultrafast HDF5 format
- Time series-specific functionality: date range generation and frequency conversion, moving window statistics, date shifting and lagging.

## Installation

```shell
pip install pandas
```

## Pandas Usage

```python
import pandas as pd
```

### Pandas Data Structures
#### Series

- a series is a one dimensional labeled array capable of holding any data type

```python
s = pd.Series([3, -5, 7, 4], index=["a", "b", "c", "d"])
```

#### DataFrame

- a dataframe is a two dimensional labeled data structure with columns of potentially different types

```python
data = {"Country": ["Belgium", "India", "Brazil"],
	"Capital": ["Brussels", "New Delhi", "Brasilia"],
	"Population": [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data, columns=["Country", "Capital", "Population"]
```

### Selection
#### Getting
#### Selecting, Boolean Indexing & Setting

### Dropping

### Sort & Rank

### Retrieving Series/DataFrame Information
#### Basic Information
#### Summary

### Applying Functions

### Data Alignment
#### Internal Data Alignment
#### Arithmetic Operations with Fill Methods

### I/O
#### Read and Write to CSV
#### Read and Write to Excel
#### Read and Write to SQL Query or Database Table
