class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        p=0
        for i in range(1,len(prices)):
            p=max(p,prices[i]-mini)
            mini=min(mini,prices[i])
        return p
            
