class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect cycle
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Phase 2: Find entrance to cycle
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
