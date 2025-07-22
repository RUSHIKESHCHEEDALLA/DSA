class Solution(object):
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        def hr1(nums):
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
        rl=hr1(nums[:len(nums)-1])
        rf=hr1(nums[1:])
        # print(rl)
        # print(rf)
        return max(rl,rf)

            