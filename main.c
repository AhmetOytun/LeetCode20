int search(int* nums, int numsSize, int target){
    int l=0,h=numsSize-1;
    while (l<=h){
        int m=(h+l)/2;
        if (nums[m]>target){
            h=m-1;
        }else if(nums[m]<target){
            l=m+1;
        }else{
            return m;
        }
    }
    return -1;

}