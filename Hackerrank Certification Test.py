def findSubstring(s: str, k: int):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowelcnt = curvowel = prevvowel = 0
    sol = ""
    temp = ""

    for x in s:
        if x in vowels:
            vowelcnt += 1

    if vowelcnt == 0:
        return "Not found!"

    for x in range(len(s)-k+1):

        for y in range(x, x + k):
            if s[y] in vowels:
                curvowel += 1
            temp += s[y]

        if curvowel > prevvowel:
            sol = temp
            prevvowel = curvowel

        curvowel=0
        temp=""
    return sol

print(findSubstring("azerdii",5))

def filledOrders(order, k):
    sol=0
    order.sort()
    for x in order:
        if x<=k:
            k-=x
            sol+=1
    return sol

print(filledOrders([10,30],40))