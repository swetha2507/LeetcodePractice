# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        res = ""
        min_length = len(strs[0])

        for string in strs:
            if len(string) < min_length:
                min_length = len(string)
        
        for i in range(min_length):
            common_letter = strs[0][i]
            for j in range(1,len(strs)):
                if common_letter != strs[j][i]:
                    return res
            res += common_letter
        return res