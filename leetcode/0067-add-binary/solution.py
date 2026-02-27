class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        sumString = ''
        lena = len(a)
        lenb = len(b)

        for i in range(1,min(lena,lenb)+1):
            if a[-i] == '0' and b[-i] == '0' and carry == 0:
                sumString  = '0' + sumString
            elif a[-i] == '0' and b[-i] == '0' and carry == 1:
                sumString  = '1' + sumString
                carry = 0
            elif a[-i] == '1' and b[-i] == '0' and carry == 0:
                sumString  = '1' + sumString
            elif a[-i] == '1' and b[-i] == '0' and carry == 1:
                sumString  = '0' + sumString
            elif a[-i] == '0' and b[-i] == '1' and carry == 0:
                sumString  = '1' + sumString
            elif a[-i] == '0' and b[-i] == '1' and carry == 1:
                sumString  = '0' + sumString
            elif a[-i] == '1' and b[-i] == '1' and carry == 0:
                sumString  = '0' + sumString
                carry = 1
            elif a[-i] == '1' and b[-i] == '1' and carry == 1:
                sumString  = '1' + sumString
        
        i = i+1
        if lena>lenb:
            while i<=lena:
                if a[-i]=='1' and carry == 1:
                    sumString = '0' + sumString 
                elif a[-i] == '1' and carry == 0:
                    sumString = '1' + sumString 
                elif a[-i] == '0' and carry == 1:
                    sumString = '1' + sumString 
                    carry = 0
                elif a[-i] == '0' and carry == 0:
                    sumString = '0' + sumString 
                i += 1
        else:
            while i<=lenb:
                if b[-i]=='1' and carry == 1:
                    sumString = '0' + sumString 
                elif b[-i] == '1' and carry == 0:
                    sumString = '1' + sumString 
                elif b[-i] == '0' and carry == 1:
                    sumString = '1' + sumString 
                    carry = 0
                elif b[-i] == '0' and carry == 0:
                    sumString = '0' + sumString 
                i += 1
        if carry:
            sumString = '1' + sumString
        
        return sumString
