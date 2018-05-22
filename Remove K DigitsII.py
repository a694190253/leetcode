# Given a non-negative integer num represented as a string;
# remove k digits from the number so that the new number is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# Runtime: 68 ms

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        arr = []
        length = len(num) -k
        if len(num) == k:
            return '0'
        for i in num:
            while k and arr and arr[-1] > i:
                arr.pop()
                k-=1
            arr.append(i)
        return "".join(arr[:length or None]).lstrip("0") or '0'

s = Solution()
res = s.removeKdigits('1173',2)
print(res)