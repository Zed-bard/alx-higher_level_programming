# 0x09. Python - Everything is object

## Description
This project delves into the concept that "everything is an object" in Python, exploring how Python works with different types of objects. The goal is to gain a deeper understanding of object behavior and how variables interact with each other.

## Background Context
In this project, we pause to examine Python's handling of various object types, emphasizing the fact that everything in Python is an object. The exploration includes scenarios where variables may be modified unintentionally or without explicit intent. For example:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
```

And another example involving lists:

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
```

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All script files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All script files should end with a newline character
- The first line of all script files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code should adhere to the `pycodestyle` guidelines (version 2.8.*)
- All script files must be executable
- The length of script files will be tested using `wc`

### .txt Answer Files
- Only one line
- No Shebang
- All files should end with a newline character

## Example
For instance, consider the following directory structure:

```
0x09-python-object_introduction/
│-- 0-answer.txt
│-- 1-answer.txt
│-- 2-answer.txt
│-- 3-answer.txt
│-- 4-answer.txt
│-- 5-answer.txt
│-- 6-answer.txt
│-- 7-answer.txt
│-- 8-answer.txt
│-- 9-answer.txt
│-- 10-answer.txt
│-- 11-answer.txt
│-- 12-answer.txt
│-- 13-answer.txt
│-- 14-answer.txt
│-- 15-answer.txt
│-- 16-answer.txt
│-- 17-answer.txt
│-- 18-answer.txt
│-- 19-copy_list.py
│-- 100-magic_string.py
│-- 101-locked_class.py
│-- README.md
```

## Author
[Zerihun Shiferaw] ([https://github.com/Zed-bard/alx-higher_level_programming])
