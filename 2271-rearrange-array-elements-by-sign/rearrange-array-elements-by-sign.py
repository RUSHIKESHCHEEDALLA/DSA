class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        # print(p)
        # print(n)
        j=0
        for i in range(len(p)):
            nums[j]=p[i]
            nums[j+1]=n[i]
            j+=2
        return nums




        