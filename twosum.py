def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums=[2,7,11,15]
target=9

print(two_sum_brute(nums,target))


def two_sum_optimized(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[num] = i 

print(two_sum_optimized(nums,target))

def two_sum_2_pointers(nums, target):
    n=len(nums)
    l=0
    r=n-1 

    while l<r:
        sum=nums[l] + nums[r]
        if sum==target:
            return [l,r]
        elif sum < target:
            l+=1 
        else:
            r-=1 
        
print(two_sum_2_pointers(nums,target))