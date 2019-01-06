import fractions as fractions

class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        leastCommonMult = abs(p * q) / fractions.gcd(p,q) if p and q else 0

        y = leastCommonMult / p
        x = leastCommonMult

        print("X %d" % x)
        print("Y %d" % y)

        return leastCommonMult
        
if __name__ == '__main__':
    print(Solution().mirrorReflection(2,1))
    print(Solution().mirrorReflection(3,1))
    print(Solution().mirrorReflection(4,1))
    print(Solution().mirrorReflection(5,1))
    
    print(Solution().mirrorReflection(3,2))