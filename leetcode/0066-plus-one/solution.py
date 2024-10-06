class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if (digits[i]+carry)>=10 :
                carry = (digits[i]+carry)//10
                digits[i] = (digits[i]+carry)%10
            else:
                digits[i] = digits[i]+carry
                carry=0

        digits = [carry]+digits if carry else digits
        return digits
