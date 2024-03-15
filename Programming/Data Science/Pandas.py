# What is Pandas?
# Pandas is a popular open-source data manipulation and analysis library for the Python programming language. 
# It provides a powerful and flexible set of tools for working with structured data.

# Here are some key features and functionalities of Pandas:

# Data Structures: Pandas offers two primary data structures - DataFrame and Series.
# Data Import and Export: Pandas makes it easy to read and write data from various sources.
# Data Merging and Joining: Combine multiple DataFrames to create more complex datasets.
# Efficient Indexing: Pandas provides efficient methods for indexing and selection.
# Custom Data Structures: Create custom data structures to suit specific needs.

# Importing Pandas:
import pandas as pd

# Data Loading:
# Pandas can be used to load data from various sources, such as CSV and Excel files.
# The read_csv function is used to load data from a CSV file into a Pandas DataFrame.
# Replace 'your_file.csv' with the actual file path of your CSV file.
df = pd.read_csv('your_file.csv')

# What is a Series?
# A Series is a one-dimensional labeled array in Pandas.
# It can be thought of as a single column of data with labels or indices for each element.

# Creating a Series:
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Accessing Elements in a Series:
# You can access elements in a Series using index labels or integer positions.
print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label

# Series Attributes and Methods:
# Pandas Series come with various attributes and methods.
print(s.values)     # Returns the Series data as a NumPy array.
print(s.index)      # Returns the index (labels) of the Series.
print(s.shape)      # Returns a tuple representing the dimensions of the Series.
print(s.size)       # Returns the number of elements in the Series.

# What is a DataFrame?
# A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types.

# Creating DataFrames from Dictionaries:
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# Column Selection:
# Select a single column or multiple columns from a DataFrame.
print(df['Name'])  # Access the 'Name' column

# Accessing Rows:
# Access rows by index using .iloc[] or by label using .loc[].
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

# Slicing:
# Slice DataFrames to select specific rows and columns.
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# Finding Unique Elements:
# Use the unique method to determine unique elements in a column of a DataFrame.
unique_dates = df['Age'].unique()

# Conditional Filtering:
# Filter data in a DataFrame based on conditions using inequality operators.
high_above_25 = df[df['Age'] > 25]

# Saving DataFrames:
# Save a DataFrame to a CSV file using the to_csv method.
df.to_csv('trading_data.csv', index=False)

# DataFrame Attributes and Methods:
# DataFrames provide numerous attributes and methods for data manipulation and analysis.
print(df.shape)          # Returns the dimensions of the DataFrame.
print(df.info())         # Provides a summary of the DataFrame.
print(df.describe())     # Generates summary statistics for numerical columns.
print(df.head())         # Displays the first few rows of the DataFrame.
