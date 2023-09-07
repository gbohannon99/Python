# Algorithms Repository

This repository contains various sorting algorithms implemented in Python. It serves as a learning resource for understanding and implementing different sorting techniques. You can use these algorithms as reference material, study guides, or integrate them into your projects.

For each of how my sorts I used the random library so I could generate random values every time to be sorted through. I have it to where the values are printed before and after each sort so you get an 
  understanding of what they looked like before the sort. Below these how-to's are generic to help get you started 

## Table of Contents

1. [Bubble Sort](#bubble-sort)
2. [Quick Sort](#quick-sort)
3. [Merge Sort](#merge-sort)
4. [Insertion Sort](#insertion-sort)
5. [Selection Sort](#selection-sort)
6. [Contributing](#contributing)

## Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### How to Use

```python
# Usage example
from sorting_algorithms import bubble_sort

my_list = [4, 2, 9, 1, 5]
sorted_list = bubble_sort(my_list)
print(sorted_list)
```

## Quick Sort

Quick Sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer strategy to sort elements.

### How to Use

```python
# Usage example
from sorting_algorithms import quick_sort

my_list = [4, 2, 9, 1, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)
```

## Merge Sort

Merge Sort is a divide-and-conquer algorithm that divides an unsorted list into 'n' sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

### How to Use

```python
# Usage example
from sorting_algorithms import merge_sort

my_list = [4, 2, 9, 1, 5]
sorted_list = merge_sort(my_list)
print(sorted_list)
```

## Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.

### How to Use

```python
# Usage example
from sorting_algorithms import insertion_sort

my_list = [4, 2, 9, 1, 5]
sorted_list = insertion_sort(my_list)
print(sorted_list)
```

## Selection Sort

Selection Sort is an in-place comparison sorting algorithm. It divides the input list into two parts: a sorted sublist and an unsorted sublist. The algorithm repeatedly finds the minimum element from the unsorted sublist and moves it to the end of the sorted sublist.

### How to Use

```python
# Usage example
from sorting_algorithms import selection_sort

my_list = [4, 2, 9, 1, 5]
sorted_list = selection_sort(my_list)
print(sorted_list)
```

## Contributing

If you'd like to contribute to this repository by adding new algorithms, improving existing ones, or providing better documentation, please feel free to open a pull request. Your contributions are highly appreciated!


