class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                # Find the smallest bit that is 0. 
                # Since n is odd, the LSB is 1. We want the top of the trailing 1s.
                # Actually, a simpler trick: find the first bit that is 0 starting from LSB,
                # then the bit *before* that is the one we want to flip.
                
                # Example n = 11 (1011). 
                # Bit 0 is 1. Bit 1 is 1. Bit 2 is 0.
                # The trailing ones are bits 0 and 1. We flip bit 1.
                
                temp = 1
                while (n & temp) != 0:
                    temp <<= 1
                
                # temp is now at the first 0 bit.
                # The bit we want to turn off is temp >> 1
                ans.append(n - (temp >> 1))
        return ans