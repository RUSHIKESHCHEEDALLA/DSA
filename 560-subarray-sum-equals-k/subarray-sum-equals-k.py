class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ps=0
        ans=0
        hset={0:1}
        for i in nums:
            ps+=i
            if ps-k in hset:
                ans+=hset[ps-k]
            if ps in hset:
                hset[ps]+=1
            else:
                hset[ps]=1
        print(hset)
        return ans        