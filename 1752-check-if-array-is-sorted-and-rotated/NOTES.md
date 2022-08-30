**Logic:**
In a sorted array a[i] > a[i+1] only once i.e last and first element. Reset all the elements would be a[i]<a[i+1]. \n
**How?**
1. Check for a[i]>a[i+1] if True then add it to counter
2. If at any point his counter exceeds 1 return False
​