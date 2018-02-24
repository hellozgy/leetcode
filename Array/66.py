class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0]==0:return [1]
        
        tag = 0
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i]+ (1 if i==len(digits)-1 else 0) + tag
            digits[i]=sum%10
            tag = sum//10
            if tag==0:break
        if tag == 1:
            digits.insert(0, 1)
        return digits