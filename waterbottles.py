def numWaterBottles(numBottles: int, numExchange: int) -> int:
    res = 0
    empty_bottles = 0
    res += numBottles
    empty_bottles = numBottles
    numBottles = 0

    # then see if you can exchange any of the bottles
    while empty_bottles >= numExchange:
        numBottles = empty_bottles // numExchange
        empty_bottles -= numBottles * numExchange
        res += numBottles
        empty_bottles += numBottles
        numBottles = 0
    
    return res
        
print(numWaterBottles(9,3))