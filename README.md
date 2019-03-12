# Word Count Exercise in Python

## About

Simple exercise demonstrating Python's file streaming and data manipulation capabilities.

This program processes a file that contains people's names and outputs some counts as well as some transformed data.

Input:

An arbitrary file with in the following format:

```
[...]
Graham, Mckenna -- ut
    Voluptatem ipsam et at.
Marvin, Garfield -- non
    Facere et necessitatibus animi.
McLaughlin, Mariah -- consequatur
    Eveniet temporibus ducimus amet eaque.
Lang, Agustina -- pariatur
    Unde voluptas sit fugit.
[...]
```

The program can be tested on much (e.g., 100x) larger files.

Output:

1. The unique count of full, last, and first names (i.e., duplicates are counted only once)
2. The ten most common last names (the names and number of occurrences sorted in descending order)
3. The ten most common first names (the names and number of occurrences sorted in descending order)
4. A list of 25 modified names where no previous name has the same first name or same last name



## Requirements

- Python 2.7 or greater



## Running

```shell
% python word_counts.py
```



### License

MIT License

Copyright (c) 2018 George P. Stathis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
