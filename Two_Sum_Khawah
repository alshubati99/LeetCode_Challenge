class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to map numbers to their indices
        num_to_index = {}

        # Iterate through the nums list
        for i, num in enumerate(nums):
            # Compute the complement
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If it does, return the indices of the current number and the complement
                return [num_to_index[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
