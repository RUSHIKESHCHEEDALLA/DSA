class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        k=len(nums)-k
        temp=[]
        for i in range(k):
            temp.append(nums[i])
        # print(temp)
        for i in range(k,len(nums)):
            nums[i-k]=nums[i]
        # print(nums)
        for i in range(len(nums)-k,len(nums)):
            nums[i]=temp[i-len(nums)+k]
        return nums
            