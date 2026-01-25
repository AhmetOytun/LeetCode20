from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
                return 0 # Tek kişi varsa fark yoktur.
                
        nums.sort() # Önce sırala: [2, 4, 6, 10, 20, 50]
        
        min_fark = float('inf') # Sonsuz büyük bir sayı ile başlat
        
        # Pencereyi kaydırarak gez
        # i, pencerenin en sağındaki (en büyük) elemanı temsil eder
        for i in range(k - 1, len(nums)):
            en_buyuk = nums[i]
            en_kucuk = nums[i - k + 1] # Pencerenin en solu
            
            fark = en_buyuk - en_kucuk
            
            if fark < min_fark:
                min_fark = fark
                
        return min_fark