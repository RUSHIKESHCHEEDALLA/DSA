class Solution(object):
    def possibleStringCount(self, word):
        h=[]
        s=[]
        for i in word:
            if len(s)==0:
                s.append(i)
            elif len(s)>0:
                if str(s[-1])==i:
                    s.append(i)
                else:
                    h.append(len(s))
                    s=[]
                    s.append(i)
        h.append(len(s))
        print(h)
        ans=1
        for i in h:
            if i>1:
                ans+=i-1
        return ans
        