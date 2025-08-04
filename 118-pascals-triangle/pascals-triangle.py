class Solution(object):
    def generate(self, numRows):
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
                    # print(s)
                    for i in range(1,len(s)):
                        val=s[i-1]+s[i]
                        # print(val)
                        ans.append(val)
                    ans.append(1)
                    # print(ans)
                    a.append(ans) 
            return a
        return fa(numRows,[])
       





        