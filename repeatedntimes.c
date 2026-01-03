int search(int *arr, int size, int target)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == target)
        {
            return 1;
        }
    }
    return 0;
}

int repeatedNTimes(int *nums, int numsSize)
{
    int dict[2501] = {0};
    int count = 0;

    for (int i = 0; i < numsSize; i++)
    {
        if (search(dict, count, nums[i]))
        {
            return nums[i];
        }
        else
        {
            dict[count++] = nums[i];
        }
    }
}