class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        int_list = (str(i) for i in digits)
        num=int(''.join(int_list))
        num+=1
        digits = [char for char in str(num)]
        return(digits)
    