"""
Since the array nums is already sorted, all duplicate values will be adjacent to each other.

Use two pointers:
Pointer i (slow pointer): Keeps track of the position where the next unique element should be placed.
Pointer j (fast pointer): Iterates through the array to find unique elements.

Start with i = 0, since the first element is always unique.

Iterate through the array with j starting from index 1.

If nums[j] is different from nums[i], increment i and update nums[i] with nums[j].

After the loop, i + 1 represents the count of unique elements.

Time Complexity: O(n), because we iterate once.
Space Complexity: O(1), since we modify in place.


"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 # empty array
        
        i = 0  # pointer for unique elements
           
        for j in range(1, len(nums)) : #iterate from second element
            if nums[j] != nums[i] :  # unique element
                i+=1 # move pointer for unique element
                nums[i] = nums[j]    # place unique element at correct position
        return i+1  # number of unique elements


nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k, nums[:k]) #output: 5, nums = [0,1,2,3,4]



  