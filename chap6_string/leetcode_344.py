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
        # s.reverse()
s = ["h","e","l","l","o"]
# def reverseString(s):
#     new_s = []
#     for i in range(len(s)-1, -1, -1):
#         new_s.append(s[i])

#     for i in range(len(s)):
#         s[i] = new_s[i]

# print(reverseString(s))
s.reverse()
print(s)