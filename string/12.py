class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['I', 'II', 'III', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        digit = [1, 2, 3, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res= ''
        for i in range(len(roman)-1, -1,-1):
            while num>=digit[i]:
                res+=roman[i]
                num-=digit[i]
        return res