def find_max_min(nums):
    min_ = min(nums) 
    max_ = max(nums)
    if min_ == max_:
        return [len(nums)]
    else:
        return [min_, max_]
