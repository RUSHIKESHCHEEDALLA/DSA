class Solution(object):
    def maximumLength(self, nums):
        c1=sum(1 for x in nums if x%2==0)
        c2=sum(1 for x in nums if x%2!=0)
        e=o=0
        for x in nums:
            if x%2==0:
                e=max(e,o+1)
            else:
                o=max(o,e+1)
        return max(c1,c2,e,o)

