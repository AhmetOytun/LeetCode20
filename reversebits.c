#include <stdio.h>

int reverseBits(int n)
{
    int result = 0;

    for (int i = 0; i < 32; i++)
    {
        // 1. Result'ı sola kaydırarak yeni bit için yer aç
        result = result << 1;

        // 2. n'in son bitini (LSB) al ve result'ın sonuna ekle
        if ((n & 1) == 1)
        {
            result = result ^ 1; // veya result = result + 1;
        }

        // 3. n'i sağa kaydırarak bir sonraki bite geç
        n = n >> 1;
    }

    return result;
}

int main()
{
    int res = reverseBits(43261596);

    printf("%d", res);

    return 0;
}