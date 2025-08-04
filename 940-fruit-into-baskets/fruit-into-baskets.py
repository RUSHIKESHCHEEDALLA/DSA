class Solution(object):
    def totalFruit(self, fruits):
        l=0
        ans=0
        h={}
        for r in range(len(fruits)):
            if fruits[r] in h:
                h[fruits[r]]+=1
            else:
                h[fruits[r]]=1
            
            if len(h)>2:
                h[fruits[l]]-=1
                if h[fruits[l]]==0:
                    del h[fruits[l]]
                l+=1
            else:
                ans=max(ans,r-l+1)
        return ans
                

        