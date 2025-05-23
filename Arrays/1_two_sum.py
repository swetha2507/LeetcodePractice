# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 16.9M
# Submissions
# 30.5M
# Acceptance Rate
# 55.4%
# Topics

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums):
            if n not in hashmap:
                hashmap[n] = i 
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in hashmap:
                if hashmap[diff] != i:
                    return [hashmap[diff], i] 