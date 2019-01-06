class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        uniqueEmails = []
        for e in emails:
            split_email = e.split("@")
            emaildecomp = split_email[0].replace(".","").split("+")[0] + "@" + split_email[1]
            if emaildecomp not in uniqueEmails:
                uniqueEmails.append(emaildecomp)
                count+=1
        return count
if __name__ == '__main__':
    print(Solution().numUniqueEmails(["test@email.com", "test+plus@email.com"]))