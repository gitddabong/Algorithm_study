class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """
        new_s = []
        for i in range(len(s)-1, -1, -1):
            new_s.append(s[i])

        s = new_s
        """
        s.reverse()