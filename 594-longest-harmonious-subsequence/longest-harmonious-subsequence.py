class Solution(object):
    def findLHS(self, nums):
        h=Counter(nums)
        ans=0
        for k in h:
            #print(k)
            if(k+1 in h):
                ans=max(ans,h[k]+h[k+1])
        return ans
        