class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        check = 0
        for each in data:
            if check == 0:
                if each>>7 == 0b0:
                    check = 0
                elif each>>5 == 0b110:
                    check = 1
                elif each>>4 == 0b1110:
                    check = 2
                elif each>>3 == 0b11110:
                    check = 3
                else:
                    return False
            else:
                if each>>6 != 0b10:
                    return False
                check -= 1
        print(bin(255),check)
        return check == 0