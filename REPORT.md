# MSCS-532 Algorithms and Data Structures
# Assignment:3- Algorithm Performance Analysis: Randomized Quicksort & Chaining Hash Table

## 1. Introduction

This report explores the design, implementation, and performance evaluation of two fundamental algorithms in computer science: Randomized Quicksort and a Hash Table with Chaining. The aim is to understand how these algorithms behave under different conditions, evaluate their efficiency, and analyze their practical applicability. Both algorithms are implemented in Python and tested using a variety of data types, including integers, strings, and mixed values, to assess their robustness and performance.

## 2. Randomized Quicksort

### 2.1 Algorithm Description

Randomized Quicksort is an improvement over the classical Quicksort algorithm, where the pivot is chosen randomly from the subarray during partitioning. This randomization reduces the probability of worst-case performance, which can occur in deterministic pivot selection when the input is already sorted or reverse-sorted. The algorithm recursively partitions the array into elements smaller than or equal to the pivot and elements greater than the pivot, and continues sorting these subarrays until the base case of a single-element or empty array is reached.

### 2.2 Theoretical Analysis

The expected runtime of Randomized Quicksort can be expressed with the recurrence relation:
[
T(n) = T(k) + T(n-k-1) + \Theta(n)
]
where k represents the number of elements less than or equal to the randomly selected pivot. Using indicator random variables for pairwise comparisons, the expected number of comparisons results in an average-case time complexity of O(n log n). Random pivot selection ensures that consistently poor partitions are highly unlikely, making the algorithm reliable across different input types.

### 2.3 Empirical Evaluation

To assess practical performance, both Randomized and Deterministic Quicksort were tested on arrays of various sizes and distributions:

* Random arrays containing numbers from 1 to 50.
* Already sorted arrays.
* Reverse-sorted arrays.
* Arrays with repeated elements such as [2, 5, 7, 10].

Results show that Randomized Quicksort maintains stable runtimes across all distributions. Deterministic Quicksort demonstrates significant slowdowns on sorted or reverse-sorted arrays due to suboptimal pivot choices. Minor variations from theoretical expectations are attributed to implementation overhead in Python.

## 3. Hash Table with Chaining

### 3.1 Implementation Details

The Hash Table employs chaining to handle collisions, using a list of lists where each sublist represents a chain of elements hashed to the same index. The key operations implemented are:

* **Insert:** Adds a key-value pair, updating the value if the key already exists.
* **Search:** Retrieves the value for a given key.
* **Delete:** Removes the key-value pair if present.

To ensure efficiency, the table dynamically doubles its size when the load factor exceeds 0.7, redistributing existing entries across the expanded table to minimize collisions.

### 3.2 Test Cases

The hash table was evaluated using different types of keys:

* Integer keys: [11, 34, 7, 11, 29, 3]
* String keys: ["pear", "mango", "cherry", "pear", "plum"]
* Mixed keys: [202, "kiwi", 58, "peach", 202]

These tests confirm correct insertion, updating of duplicate keys, search functionality, deletion, and proper resizing of the table.

### 3.3 Performance Analysis

Assuming uniform hashing, the expected time complexity of insert, search, and delete operations is O(1 + α), where α is the load factor. Chaining ensures that even with collisions, average chain lengths remain short, allowing efficient operations. Dynamic resizing prevents degradation of performance as the number of entries increases.

## 4. Observations and Discussion

The analysis highlights the reliability and effectiveness of both algorithms. Randomized Quicksort delivers consistent performance, mitigating the risk of worst-case behavior inherent in deterministic approaches. The Chaining Hash Table demonstrates efficient storage, retrieval, and management of diverse key types, handling collisions effectively while maintaining low operation times.

Empirical testing aligns closely with theoretical predictions, reinforcing the importance of algorithmic design choices such as randomization in sorting and dynamic resizing in hash tables. The combination of theoretical and practical evaluation illustrates how these algorithms can be applied to real-world data efficiently.


## 5. Conclusion

Randomized Quicksort is a robust sorting solution capable of efficiently handling varied data distributions, while Hash Tables with Chaining provide an effective data structure for managing key-value pairs with high efficiency. Both algorithms demonstrate the importance of algorithmic design considerations, balancing theoretical complexity with practical performance. This analysis confirms that careful implementation and evaluation are critical for selecting appropriate algorithms for specific applications.

