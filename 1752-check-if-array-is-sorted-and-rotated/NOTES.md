**Logic:**
In a sorted array a[i] > a[i+1] only once i.e last and first element. Reset all the elements would be a[i]<a[i+1].
**How?**
1. Check for a[i]>a[i+1] if True then add it to counter
2. If at any point his counter exceeds 1 return False
​
Code:
class Solution:
def check(self, nums: List[int]) -> bool:
N = len(nums);k =0
for i in range(N):
if nums[i]>nums[(i+1)%N]:
k += 1
if k> 1:
return False
return True