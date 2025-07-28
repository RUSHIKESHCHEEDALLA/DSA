class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=n*(n+1)//2
        # print(ans)
        s=0
        for i in nums:
            s+=i
        # print(s)
        return ans-s
        