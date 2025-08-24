# def first_accurance(nums, target):
#     low, high = 0 , len(nums) -1
#     first = -1
#     while low<=high:
#         mid = (low + high )// 2
#         if nums[mid] == target:
#             first=mid
#             high=mid-1
#         elif nums[mid] < target:
#             low = mid +1
#         else:
#             high = mid-1
#     return first

# def last_accurance(nums, target):
#     low, high = 0 , len(nums) -1
#     last = -1
#     while low<=high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             last=mid
#             low=mid+1
#         elif nums[mid] < target:
#             low = mid +1
#         else:
#             high = mid-1
#     return last

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(first_accurance(nums , target) , last_accurance(nums , target))

##############################################################################################

def first_accurance(nums, target):
    low, high = 0 , len(nums) -1
    first = 0
    while low<=high:
        mid = (low + high )// 2
        if nums[mid] == target:
            first = mid
            return first
        elif nums[mid] < target:
            low = mid +1
            if(nums[low+1] <= target):
                return first+1
        else:
            high = mid-1
            if(nums[high-1] >= target):
                return first+1
    return first

nums = [5, 7, 7, 8, 8, 10]
target = 60
print(first_accurance(nums , target))