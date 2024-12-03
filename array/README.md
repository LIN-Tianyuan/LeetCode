# Array

An array is a collection of the same type of data stored on a contiguous memory space.

Arrays can be easily accessed by means of subscript indexing to the data corresponding to the subscript.

<b>Array subscripts all start at 0.
Addresses in the array memory space are contiguous.</b>

It is because arrays have contiguous addresses in memory space that we inevitably have to move the addresses of other elements when we delete or add elements.

<b> Elements of an array cannot be deleted, only overwritten. </b>

### 1. Binary search(704)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#### Idea
The premise of this question is that the array is an ordered array, at the same time, the topic also emphasizes that there are no repetitive elements in the array, because once there are repetitive elements, the use of bisection to find the return of the element subscripts may not be unique, these are the prerequisites for the use of the method of binary search.

#### Code
Time complexity: O(log n)
Space complexity: O(1)

### 2. Search Insert Position(35)
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.





## License

[MIT](https://choosealicense.com/licenses/mit/)