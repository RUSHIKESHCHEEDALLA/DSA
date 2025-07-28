class Solution(object):
    def missingNumber(self, nums):
        v=[ 0 for _ in range(len(nums)+1)]
        for i in nums:
            v[i]=1
        # print(v)
        for i in range(len(v)):
            if v[i]==0:
                return i