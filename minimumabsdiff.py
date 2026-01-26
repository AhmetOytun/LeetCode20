from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Diziyi sırala
        min_fark = float('inf')  # Başlangıçta sonsuz büyük bir fark
        sonuc = []  # Sonuç listesi
        
        # Ardışık elemanlar arasındaki farkları kontrol et
        for i in range(1, len(arr)):
            fark = arr[i] - arr[i - 1]
            
            if fark < min_fark:
                min_fark = fark
                sonuc = [[arr[i - 1], arr[i]]]  # Yeni minimum fark bulundu, listeyi güncelle
            elif fark == min_fark:
                sonuc.append([arr[i - 1], arr[i]])  # Aynı minimum fark bulundu, listeye ekle
                
        return sonuc