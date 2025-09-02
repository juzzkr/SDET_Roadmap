def max_no(nums):
    maxi = nums[0]
    for n in nums:
        if n > maxi:
            maxi = n
    return maxi

print(max_no([1,5,34,5,2,6]))