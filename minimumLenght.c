#include <stdio.h>
#include <string.h>
int minimumLength(char* s) {
    int length = strlen(s);
    int l = 0;
    int r = length-1;

    while(l<r&&s[l]==s[r]){
        char c = s[l];
        while(l<=r&&s[l]==c){
            l+=1;
        }
        while(r>=l&s[r]==c){
            r-=1;
        }
    }

    return r-l+1;
}
int main(void){
    char s[] = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbacccabbabccaccbacaaccacacccaccbbbacaabbccbbcbcbcacacccccccbcbbabccaacaabacbbaccccbabbcbccccaccacaccbcbbcbcccabaaaabbbbbbbbbbbbbbb";
    int solution = minimumLength(s);
    printf("%d\n", solution);
    return 0;
}