class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hs={}
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in hs:
                # print(i)
                # print(nums[i]-target)
                return [i,hs[target-nums[i]]]
            
            hs[nums[i]]=i
            # print(hs)
        
            

        