# Sorting algorithms

## Working:

* [Bubble sort](#bubble-sort)
* [Insertion sort](#insertion-sort)
* [Merge sort](#merge-sort)

## Bubble sort
#### Presentation
Bubble sort is comparing adjacent numbers: if the compared pair is in the wrong order, it gets swapped, and then the algorithm is comparing the next two numbers. This process is repeated until the whole array is sorted.
#### Complexity
* Best case: *O(n)* as the algorithm is comparing each pair at least once
* Worst case: *O(n<sup>2</sup>)*

## Insertion sort
#### Presentation
Insertion sort iterates over each element, removes it from the array to place it at the correct sorted position. This process is repeated until the whole array is sorted.
#### Complexity
* Best case: *O(n)* 
* Worst case: *O(n<sup>2</sup>)*

## Merge sort
#### Presentation
Merge sort is a "divide and conquer algorithm", which means that it recursively divides the array into two evenly-sized arrays until each array contains one element. Then, the algorithm sorts each array when merging back the subarrays.
#### Complexity
* Best case: *O(n·log(n))* 
* Worst case: *O(n·log(n))*

## TBA:

* Heapsort
* Quicksort
* Shellsort
* Cocktail shaker sort
* Comb sort
* Radix sort
