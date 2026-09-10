class Solution:
    def subsets(self, nums):
        res = []
        
        def backtrack(start, path):
            res.append(path[:])  # store current subset
            for i in range(start, len(nums)):
                path.append(nums[i])       # include nums[i]
                backtrack(i + 1, path)     # move forward
                path.pop()                 # exclude nums[i]
        
        backtrack(0, [])
        return res
