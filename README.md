# bookbot

This project serves as an introduction to python with a small file reading program. <br> 
Below are some of the steps involved in this small program.

### Reading the file:
```python
with open("books/frankenstein.txt") as f:
        file_contents = f.read()
```
#### Note: 
_Since the `book` folder is in the same directory as the main.py file, the absolute file path starts with the `book` directory. A relative directory needs to be used from where the program execution file sits_

---
### Methods to sort a dictionary by keys:
```python
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
# ---------- or -------------
>>> dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```
_credit : https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value_

`dict.items()` <br>
gives a list of tuples with (key, value) pair from dict <br><br>
`sorted(iterable, key=None, reverse=False)` 
- iterable is anything like a list, tuple, set, string etc 
- key = function to execute for deciding order of elements (default is None) 
<br>

```python
>>> a = ["apple", "banana", "cherry", "date"]
>>> res = sorted(a, key=len)
>>> print(res)
['date', 'apple', 'banana', 'cherry']
# ----------------------
>>> a = [
>>>     {"name": "Alice", "score": 85},
>>>     {"name": "Bob", "score": 91},
>>>     {"name": "Eve", "score": 78}
>>> ]

# Use sorted() to sort the list 'a' based on the 'score' key
# sorted() returns a new list with dictionaries sorted by the 'score'
>>> b = sorted(a, key=lambda x: x['score'])
>>> print(b)

[{'name': 'Eve', 'score': 78}, {'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 91}]
```
---
### Printing out from dictionary

#### Loop through both key and value in dictionary:
```python
for key,value in letters_dict.items():
        print(f"The '{key}' character was found {value} times")
```

#### Loop through keys and get values from dictionary:
```python
for key in letters_dict:
        print(f"The '{key}' character was found {letters_dict[key]} times")
```