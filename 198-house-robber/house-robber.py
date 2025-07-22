class Solution(object):
    def rob(self, nums):
        # def fa(ind):
        #     if ind==0:
        #         return nums[ind]
        #     if ind<0:
        #         return 0
        #     p=nums[ind]+fa(ind-2)
        #     np=fa(ind-1)     
        #     return max(p,np) 
        # return fa(len(nums)-1)  
        dp={}
        dp[0]=nums[0]
        def fa(ind):
            if ind<0:
                return 0
            if ind in dp:
                return dp[ind]
            p=nums[ind]+fa(ind-2)
            np=fa(ind-1) 
            dp[ind]=max(p,np)    
            return dp[ind]
        return fa(len(nums)-1)
            



        