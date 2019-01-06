class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dict = {}
        for i in A :
            if i in dict:
                return i
            else:
                dict[i] = 1
        
if __name__ == '__main__':
    print(Solution().repeatedNTimes([1,2,3,3]))
    print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
    print(Solution().repeatedNTimes( [2,1,2,5,3,2]))