1.How would you remove duplicates from a list while preserving the order?
2. How do you flatten a nested list without using recursion?
3. What’s the difference between a shallow copy and a deep copy in Python? Give an example.
4. How do you merge two dictionaries in Python without overwriting values for duplicate keys?
5. Write Python code to read a large CSV file in chunks and process each chunk without loading the entire file into memory.
6. How would you parse a large JSON file in Python efficiently?
7. Given a log file with millions of lines, how do you extract the top 10 most frequent error messages?
8. How do you read and process compressed files (like .gz or .zip) in Python?
9. Write code to convert a CSV file to Parquet format using Pandas.
10. How do you handle missing values in a Pandas DataFrame? Show examples for filling and dropping them.
11. How would you merge two DataFrames on multiple keys with an inner join?
12. Given a time-series DataFrame, how would you resample data to a weekly frequency and calculate the sum?
13. How do you detect and remove outliers from a dataset using Pandas or NumPy?
14. Write code to group data by a column and compute multiple aggregate functions in a single statement.
15. How do you implement a retry mechanism in Python when an API call fails during ETL processing?
10:08 AM

Narayana
➕
def flatten_recursive(nested_list):
    """Recursively flattens a nested list of any depth."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, extend the flattened list with the result of a recursive call
            flattened.extend(flatten_recursive(item))
        else:
            # Otherwise, it's a single element, so just append it
            flattened.append(item)
    return flattened
complex_list = [1, 2, [3, [4, 5], [1, 2, [4, 5]], 7], 10]
print(flatten_recursive(complex_list))