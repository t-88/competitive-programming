
class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2: return 0 

        traped = 0        
        a , b  = 0, 0
        size = len(height)

        while a < size :
            if(height[a] == 0): 
                a +=1
                continue

            k = height[a]
            b = a + 1

            # stop when u find bigger
            # or stop when u out of range
            while(b < size and height[a] > height[b]): 
                k += height[b]
                b += 1


            if(b < size):
                # u found bigger
                traped += (b - a - 1) * min(height[a],height[b]) - k
                a = b
                continue
            else:
                # u didnt find bigger
                # check out the max and calculate using it
                # 4 1 3
                c  = max(height[a:b-1])
                d = min(height[a:b-1])
                if(height[b - 1] != 0):
                    traped += (b - a - 1) * c - k
                

            a += 1
        return traped
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))