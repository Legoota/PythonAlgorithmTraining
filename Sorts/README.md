# Sorting algorithms

## Working:

* [Bubble sort](#bubble-sort)
* [Insertion sort](#insertion-sort)
* [Merge sort](#merge-sort)
* [Coctail sort](#cocktail-sort)
* [Comb sort](#comb-sort)
* [Shell sort](#shell-sort)

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

## Cocktail sort
#### Presentation
Comb sort is an extension of the bubble sort, as it is operating in two directions. It can provide faster sorting in case of small numbers presence at the end of the array, since they will be moved sooner than with the standard bubble sort. However, it provides only small performance improvements.
#### Complexity
* Best case: *O(n)* 
* Worst case: *O(n<sup>2</sup>)*

## Comb sort
#### Presentation
Comb sort is a modified bubble sort that compares two numbers that are not necessarily next to each other. In the usual bubble sort, the gap between the two compared numbers is 1. In the comb sort, the idea is to use a gap slightly bigger than 1 (in our implementation, this gap is initialized to the size of the array, then each time we shrink it with a factor of 1.3). The goal of this method is to move small numbers at the end of the array faster than with the standard bubble sort.
#### Complexity
* Best case: *O(n·log(n))* 
* Worst case: *O(n<sup>2</sup>)*

## Shell sort
#### Presentation
Shell sort is an optimized insertion sort algorithm. The difference lies in the possibility of swapping elements that are far in the array, by using "gaps". The gap can be calculated from various methods, and depends on the array's values interval. In our implementation, we decided to use a gap the size of half the array's size, then reducing this gap by half each iteration.
#### Complexity
* Best case: *O(n·log(n))* 
* Worst case: *O(n<sup>2</sup>)*

## Quick sort
#### Presentation
To be added
#### Complexity
* Best case: *O(n·log(n))* 
* Worst case: *O(n<sup>2</sup>)*

## TBA:

* Heapsort
* Radix sort
* Timsort
