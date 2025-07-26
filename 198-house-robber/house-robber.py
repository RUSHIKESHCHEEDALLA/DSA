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
        # dp={}
        # dp[0]=nums[0]
        # def fa(ind):
        #     if ind<0:
        #         return 0
        #     if ind in dp:
        #         return dp[ind]
        #     p=nums[ind]+fa(ind-2)
        #     np=fa(ind-1) 
        #     dp[ind]=max(p,np)    
        #     return dp[ind]
        # return fa(len(nums)-1)
        # if len(nums)<=2:
        #     return max(nums)
        # dp=[0 for _ in range(len(nums))]
        # dp[0]=nums[0]
        # dp[1]=max(nums[0],nums[1])
        # print(dp)
        # for i in range(2,len(nums)):
        #     dp[i]=nums[i]+max(dp[0:i-1])
        # print(dp)
        # return max(dp[-1],dp[-2])


        if len(nums)==1:
            return nums[0]
        p2=0
        p1=nums[0]
        for i in range(1,len(nums)):
            t=nums[i]
            if i>1:
                t+=p2
            nt=p1
            c=max(t,nt)
            p2=p1
            p1=c
        return p1
        

            



        