def threeSum(nums,N):
    nums.sort()
    for n in range(len(nums)):
        target = N - nums[n]
        i,j = 0,len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                if i != n and j != n:
                    return True
                elif i == n:
                    i += 1
                else:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
    return False
