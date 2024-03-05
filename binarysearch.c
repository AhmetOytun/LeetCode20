 int search(int* nums, int numsSize, int target){
    int l=0,h=numsSize-1,m;
    while (l<=h){
        m=(h+l)/2;
        if (nums[m]==target){
            return m;
        }else if(nums[m]<target){
            l=m+1;
        }else{
            h=m-1;
        }
    }
    return -1;
}
int main(void){
    return 0;
}