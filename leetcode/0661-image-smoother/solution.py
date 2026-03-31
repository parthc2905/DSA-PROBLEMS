class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])
        smoothImg = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                _sum = 0 
                count = 0
                for k in range(-1,2):
                    for l in range(-1, 2):
                        nx,ny = i+k, j+l
                        if 0 <= nx < r and 0<= ny < c:
                            _sum += img[nx][ny]
                            count += 1

                smoothImg[i][j] = _sum//count
        return smoothImg 
                    
        
