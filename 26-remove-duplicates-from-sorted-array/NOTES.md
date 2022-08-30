* Logic:
1. As the array is sorted all the duplicates would be one after another. i.e A[i] and A[i+1] (starting with 0 index) or A[i-1] and A[i] (starting with 1 index)
2. If A[i] == A[i-1] then Increase the Count (Count represents the number of Duplicates)
3. If A[i] != A[i-1] then copy the element to i-Count position as that position has a duplicate element losing it won't affect the solution.
* Complexity : O(n) for traversing through the list