def sort(nums):
    for i in range(len(nums)-1,0,-1):     #check number of elements for iterations
        for j in range(i):               # for swapping between number
            if nums[j] > nums[j+1]:

                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums=[5,3,8,6,7,2]
sort(nums)
print(nums) 