#include <stdio.h>

int countOperations(int num1, int num2)
{
    int operation_count = 0;
    while (num1 != 0 && num2 != 0)
    {
        if (num1 > num2)
        {
            num1 = num1 - num2;
            operation_count++;
        }
        else
        {
            num2 = num2 - num1;
            operation_count++;
        }
    }

    return operation_count;
}

int main()
{
    int res = countOperations(2, 3);

    printf("%d", res);

    return 0;
}