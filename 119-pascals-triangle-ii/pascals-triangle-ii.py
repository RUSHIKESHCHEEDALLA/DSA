class Solution(object):
    def getRow(self, rowIndex):
        ans=[]
        def fa(n,a):
            if n==1:
                a.append([1])
            elif n==2:
                fa(n-1,a)
                a.append([1,1]) 
            else:
                fa(n-1,a)
                if len(a)>0:
                    s=a[-1]
                    ans=[1]
                    for i in range(1,len(s)):
                        val=s[i-1]+s[i]
                        ans.append(val)
                    ans.append(1)
                    a.append(ans) 
            return a
        ans=fa(rowIndex+1,[])
        return ans[-1]
       





        