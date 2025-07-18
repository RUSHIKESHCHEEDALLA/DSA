class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc]==color:
            return image
        pc=image[sr][sc]
        image[sr][sc]=color
        q=[[sr,sc]]
        while q:
            r,c=q.pop(0)
            d=[(-1,0),(0,1),(1,0),(0,-1)]
            for x,y in d:
                nr=r+x
                nc=c+y
                # print(image)
                if 0<=nr<len(image) and 0<=nc<len(image[0])  and image[nr][nc]==pc:
                    image[nr][nc]=color
                    q.append([nr,nc])
        return image
        