class Solution:
    def maxIncreaseKeepingSkyline(self, Grid):
        """
        :type A: List[int]
        :rtype: int
        """
        yMax = []
        xMax = []

        y = 0
        for row in Grid:
            x = 0
            for building in row:
                if len(yMax) - 1 < y:
                    yMax.append(building)                    
                if len(xMax) - 1 < x:
                    xMax.append(building)
                if building > xMax[x]:
                    xMax[x] = building
                if building > yMax[y]:
                    yMax[y] = building
                x+=1
            y+=1
        total = 0
        y = 0
        for row in Grid:
            x = 0
            for building in row:
                total+=min(xMax[x] - building, yMax[y] - building)
                x+=1
            y+=1
        return total
        
if __name__ == '__main__':
    print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],
                                                [2,4,5,7],
                                                [9,2,6,3],
                                                [0,3,1,0]]))

