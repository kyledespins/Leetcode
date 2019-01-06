class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        def CharToLowerCase(c):
            c_ascii = ord(c)
            if(c_ascii > 64 and c_ascii < 91):
                ret = c_ascii + 32
            else:
                ret = c_ascii
            return chr(ret) 
        return ''.join(map(CharToLowerCase, list(str)))
        
if __name__ == '__main__':
    print(Solution().toLowerCase("aBC"))
    print(Solution().toLowerCase("aBC111"))