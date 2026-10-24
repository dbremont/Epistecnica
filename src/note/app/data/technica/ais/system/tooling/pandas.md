---
tags: [tool]
---

# Pandas


> **Pandas** is a powerful, open-source Python library providing fast, flexible, and expressive data structures designed to make data manipulation and analysis easy and intuitive for relational or labeled data.
> 

QA:

- How to query pandas data model using a **SQL Interface**? [‣](https://app.notion.com/p/78e70fed85424f178de85442eb437802?pvs=21).
- …

## Data Model

- **`Series`**: A one-dimensional labeled array capable of holding any data type.
- **`pandas.core.frame.DataFrame`**: A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
- **`Index`**: The immutable array-like object that holds the axis labels and metadata for Series and DataFrames.

## Dataframes

> A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
> 

> Pandas DataFrames offer a wide array of functions for manipulating, querying, and analyzing tabular data.
> 

Here's a list of some of the main functions you'll frequently use:

1. **`corr()`**:  Compute pairwise correlation of columns, excluding NA/null values.
2. **`head()`**: Returns the first N rows of the DataFrame, useful for a quick preview.
3. **`tail()`**: Displays the last N rows, helpful for checking the end of your data.
4. **`describe()`**: Provides a summary of statistics for numerical columns.
5. **`info()`**: Gives a concise summary of the DataFrame, including the index dtype and columns, non-null values, and memory usage.
6. **`loc[]`**: Accesses a group of rows and columns by labels or boolean arrays.
7. **`iloc[]`**: Accesses a group of rows and columns by integer position(s).
8. **`drop()`**: Removes specified labels from rows or columns.
9. **`isnull()`** or **`isna()`**: Detects missing values.
10. **`fillna()`**: Fills NA/NaN values using a specified method.
11. **`astype()`**: Casts a pandas object to a specified dtype.
12. **`copy()`**: Returns a copy of the DataFrame.
13. **`apply()`**: Applies a function along an axis of the DataFrame.
14. **`merge()`**: Merges DataFrame or named Series objects with a database-style join.
15. **`join()`**: Joins columns of another DataFrame, similar to SQL join.
16. **`groupby()`**: Groups DataFrame using a mapper or by a series of columns.
17. **`pivot_table()`**: Creates a spreadsheet-style pivot table as a DataFrame.
18. **`sort_values()`**: Sorts by the values along either axis.
19. **`sort_index()`**: Sorts the DataFrame by its index.
20. **`reset_index()`**: Resets the index of the DataFrame, and uses the default one instead.
21. **`set_index()`**: Sets the DataFrame index using existing columns.
22. **`to_csv()`**: Writes the DataFrame to a comma-separated values (csv) file.
23. **`to_excel()`**: Writes the DataFrame to an Excel file.
24. **`to_sql()`**: Writes the DataFrame to a SQL database.
25. **`plot()`**: Makes plots of the DataFrame using the plot() method.
26. **`iterrows()`**: Iterates over DataFrame rows as (index, Series) pairs.
27. **`itertuples()`**: Iterates over DataFrame rows as namedtuples.

## Series

> Pandas Series come with a wide array of functions that enable you to manipulate and analyze data efficiently.
> 

Here's a list of some of the main functions:

1. **`.map()`**: Apply a function or mapping to each element in the Series.
2. **`.apply()`**: Similar to `.map()`, but more flexible, allowing you to apply more complex functions.
3. **`.astype()`**: Convert the Series to a specified data type.
4. **`.sum()`**: Return the sum of the values in the Series.
5. **`.mean()`**: Calculate the mean of the values.
6. **`.median()`**: Compute the median of the values.
7. **`.mode()`**: Find the mode(s) of the Series.
8. **`.min()`**: Get the minimum value.
9. **`.max()`**: Obtain the maximum value.
10. **`.std()`**: Calculate the standard deviation.
11. **`.var()`**: Compute the variance.
12. **`.describe()`**: Generate descriptive statistics that summarize the Series' values' central tendency, dispersion, and shape.
13. **`.value_counts()`**: Return a Series containing counts of unique values.
14. **`.unique()`**: Get an array of unique values in the Series.
15. **`.nunique()`**: Count the number of unique values.
16. **`.sort_values()`**: Sort the Series by its values.
17. **`.sort_index()`**: Sort the Series by its index.
18. **`.idxmax()`**: Return the index of the first occurrence of the maximum value.
19. **`.idxmin()`**: Return the index of the first occurrence of the minimum value.
20. **`.isnull()` / `.isna()`**: Detect missing values.
21. **`.notnull()` / `.notna()`**: Detect existing (non-missing) values.
22. **`.fillna()`**: Replace missing values.
23. **`.dropna()`**: Remove missing values.
24. **`.duplicated()`**: Indicate duplicate values.
25. **`.drop_duplicates()`**: Drop duplicate values.
26. **`.head()`**: Return the first `n` elements.
27. **`.tail()`**: Return the last `n` elements.
28. **`.sample()`**: Return a random sample of items.
29. **`.concat()`**: Concatenate two or more Series.
30. **`.append()`**: Append elements from another Series or list.

## Good Practice

> Using Pandas effectively and efficiently in data analysis projects involves adhering to several best practices and principles.
> 

Here's a concise list of general principles for good use of Pandas:

1. **Use Vectorization Over Loops**: Use Pandas' vectorized operations whenever possible instead of iterating over DataFrame rows. Vectorized operations are faster and more efficient.
2. **Avoid Chained Indexing**: Accessing or setting values in a DataFrame using chained indexing (e.g., `df[a][b]`) can lead to ambiguous or unexpected results. Prefer `.loc[]`, `.iloc[]`, or `.at[]` accessors for precise and clear data manipulation.
3. **Utilize Pandas Functions**: Leverage built-in Pandas functions like `.merge()`, `.groupby()`, `.pivot_table()`, and `.cut()` for data merging, grouping, reshaping, and binning. These are optimized for performance and readability.
4. **Minimize Data Copies**: Be cautious with operations that copy DataFrames or Series, as they can consume memory. Use `inplace=True` where appropriate and understand when Pandas returns a view vs. a copy.
5. **Handle Missing Data Appropriately**: Use `.isna()`, `.fillna()`, `.dropna()` to detect, fill, or drop missing values. Choose the method that best suits your data analysis needs and maintains data integrity.
6. **Use Categorical Data Types for Efficiency**: When working with string data that takes on a limited, fixed number of values, convert it to Pandas' `category` type to save on memory and speed up operations.
7. **Profile Your Pandas Code**: Utilize tools like `%timeit` in Jupyter notebooks or Python's `time` module to measure the performance of your Pandas code, helping identify bottlenecks.
8. **Keep an Eye on Memory Usage**: Large DataFrames can consume a lot of memory. Use methods like `.info(memory_usage='deep')` to monitor memory usage and consider data types (like `int8`, `float32`, etc.) that use less memory.
9. **Stay Updated with Pandas Versions**: Pandas is actively developed, with new features and performance improvements added regularly. Staying updated can help you leverage the latest functionalities and optimizations.
10. **Learn to Use MultiIndexes**: For complex data analysis, understanding and using MultiIndex (hierarchical indexes) can provide powerful ways to organize, slice, dice, and summarize data.
11. **Document Your Data Transformations**: Comment your data transformation steps extensively to ensure your code remains readable and maintainable for both you and others.
12. **Use Chunking for Large Data**: When dealing with very large datasets that don't fit into memory, use Pandas' chunking capabilities (`read_csv(chunksize=...)`) to process data in manageable pieces.

## References

- [Pandas](https://pandas.pydata.org/)
- [A Gentle Visual Intro to Data Analysis in Python Using Pandas](https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/)
- …
