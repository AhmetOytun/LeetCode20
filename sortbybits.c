/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 /**
  * I KNOW THIS CODE IS SLOW BUT I DID IT ON MY OWN AND I AM PROUD OF IT.
  */
#include "stdio.h"
#include "stdlib.h"
int countBits(int num);
int* sortByBits(int* arr, int arrSize, int* returnSize);
int cmp(const void * a, const void * b);
void normalinsertionSort(int arr[], int n);
void binaryinsertionSort(int arr[], int n);
int main(void){
    int arr[]={1024,512,256,128,64,32,16,8,4,2,1};
    int length=(sizeof(arr)/sizeof(arr[0]));
    int *returnsize =malloc(sizeof(arr));
    sortByBits(arr,length,returnsize);
    for (int i = 0; i < length; ++i) {
        printf("%d ",arr[i]);
    }
}
int* sortByBits(int* arr, int arrSize, int* returnSize){
    normalinsertionSort(arr,arrSize);
    binaryinsertionSort(arr,arrSize);
    int *sol=malloc(sizeof (arr));
    sol=arr;
    return sol;
}
int countBits(int num){
    int count=0;
    while(num){
        count+=num&1;
        num=num>>1;
    }
    return count;
}
void binaryinsertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && countBits(arr[j]) > countBits(key)) {
            printf("bo");
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
void normalinsertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}