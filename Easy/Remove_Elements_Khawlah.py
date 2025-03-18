# Use two pointers: one to iterate over the array (i) and another (k) to track where to place elements that are not equal to val.
# Move elements that do not match val to the front.

# initialize a pointer k=0 which tracks the array length
# iterate through nums with index i: if nums[i] != val, move it to nums[k] and increment k.
# first k elements of nums will now contain only elements that are not equal to val.
# return k (count of elements not equal to val)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0 # for sorting elements that are not equal to val
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[k] = nums[i] #overwrite elements
                k+=1 # move pointer for next valid element
        return k #length of modified array


solution = Solution()
nums = [3,2,2,3]
val = 3
k = solution.removeElement(nums, val)
print(k,nums)        


"""
Time Complexity: O(n) → We iterate through the array once.
Space Complexity: O(1) → We modify the array in-place without extra memory.

"""