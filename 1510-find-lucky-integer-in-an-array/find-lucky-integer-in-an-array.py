class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        f=float("-inf")
        ans=-1
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if  d[i]==i and d[i]>f:
                ans=i
                f=d[i]
        return ans

        

        