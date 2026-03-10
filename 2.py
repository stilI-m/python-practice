def two_sum_optimized(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[nums[i]] = i

print(two_sum_optimized([12, 6, 2, 1, 9, 14, 8], 17))