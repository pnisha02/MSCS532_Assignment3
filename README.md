# MSCS532_Assignment3
Assignment 3: Understanding Algorithm Efficiency and Scalability
# Algorithm Analysis Assignment

## Overview

This repository contains Python implementations and analysis of two fundamental algorithms:

1. **Randomized Quicksort vs Deterministic Quicksort**
2. **Hash Table using Chaining**

Both implementations include diverse test cases and performance comparisons. 

`Randomizedquick.py` 
Implements Randomized and Deterministic Quicksort, and compares their performance on different array distributions.                                  `HashTablewithChaining.py`           
Implements a Hash Table with Chaining including insert, search, delete operations, dynamic resizing, and tests with integer, string, and mixed keys. 
             

## How to Run

### 1. Randomized Quicksort Comparison

```bash
python Randomizedquick.py
```

* Demonstrates sorting performance on random, sorted, reverse-sorted, and repeated arrays.
* Prints array content, size, and execution times for both Randomized and Deterministic Quicksort.

### 2. Hash Table Testing

```bash
python HashTablewithChaining.py
```

* Demonstrates hash table operations: insert, search, delete.
* Inserts integer keys `[11, 34, 7, 11, 29, 3]`, string keys `["pear", "mango", "cherry", "pear", "plum"]`, and mixed keys `[202, "kiwi", 58, "peach", 202]`.
* Displays table contents, searches specific keys, and deletes sample keys.

## Summary of Findings

### Randomized Quicksort

* Provides consistent performance across all input types.
* Avoids worst-case scenarios common in Deterministic Quicksort.
* Average-case time complexity: **O(n log n)**.

### Hash Table with Chaining

* Efficient **insert**, **search**, and **delete** operations.
* Handles duplicates and updates existing keys correctly.
* Dynamic resizing maintains efficiency even as the number of elements grows.
* Expected operation time complexity: **O(1 + α)**, where α is the load factor.

