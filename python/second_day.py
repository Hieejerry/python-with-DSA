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

# def first_accurance(nums, target):
#     low, high = 0 , len(nums) -1
#     while low<=high:
#         mid = (low + high )// 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             low = mid + 1
#         else:
#             high = mid-1
#     return low

# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# print(first_accurance(nums , target))



##################################################################
# Search element in roted sorted array using binary search 

def searchInRotedSortedArr(nums, target):
    low, high = 0 , len(nums) -1
    while low <= high:
        mid = (low + high )// 2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid +1
            else:
                high = mid -1
            
    return -1
    

nums = [5, 7, 8, 9, 10, 1 , 2]
target = 8
print(searchInRotedSortedArr(nums , target))