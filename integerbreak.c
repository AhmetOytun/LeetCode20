#include "math.h"
#include "stdio.h"
int integerBreak(int n){
    if(n<4){
        return n-1;
    }else if (n % 3 == 0){
        return pow(3, floor(n / 3));
    }
    else if (n % 3 == 1){
        return pow(3, floor(n / 3)-1)*4;
    }else if(n % 3 == 2){
        return pow(3, floor(n / 3))*2;
    }
}
int main(void){
    printf("%d", integerBreak(10));
    return 0;
}