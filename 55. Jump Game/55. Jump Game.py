class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach=0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            else:
                maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) -1:
                return True
        
obj=Solution()
print(obj.canJump([2,3,1,1,4]))                
