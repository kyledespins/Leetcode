class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        list_J = list(J)
        for c in list(S):
            if c in list_J:
                count+=1
        return count

if __name__ == '__main__':
    print(Solution().numJewelsInStones("ab", "aabbc"))