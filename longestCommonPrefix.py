# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

strs1 = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

strs2 = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        if len(strs) == 0: return ""

        for i in range(1, len(strs)):
            while strs[i].find(prefix) !=0:
                prefix = prefix[:-1]
        return prefix
    
    


            
            
        
    
result = Solution().longestCommonPrefix(strs1)

print(f'result {result}')