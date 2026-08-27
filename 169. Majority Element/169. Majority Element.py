class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
            i+=1
        return max(count,key=count.get)

obj=Solution()
print(obj.majorityElement([3,3,4]))
