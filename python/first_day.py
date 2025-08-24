# def reverse_string(s):
#     rev_str = []
#     for char in s:
#         rev_str.insert(0,char)
#     return ''.join(rev_str)


# arr = reverse_string('raushan')
# print(arr)
###################################################        
# def find_max(nums):
#   result = nums[0]
#   for num in nums[1:]:
#     if result <= num:
#         result= num
#   return result

# maxNum = find_max([1,3,15,7,9]);
# print(maxNum)

#####################################################
# def palindrome(s):
#     s = s.lower()
#     left , right = 0 , len(s) - 1
#     while left<=right:
#         if s[left] !=s[right]:
#             return 'False'
#         left +=1
#         right -=1
#     return 'true'
# print(palindrome('madam'))
                
#####################################################


# def arrSum(nums):
#     left , right = 1 , len(nums) - 1
#     while left<=right:
#         nums[0] = nums[0] + nums[left]
#         left +=1
#     return nums[0]

# print(arrSum([1, 2, 3, -4]))

########################################################

# def remove_duplicate(nums):
#     newArr = []
#     for num in nums:
#         if num in newArr:
#             continue
#         else:
#             newArr.append(num)
#     return newArr

# print(remove_duplicate([1, 2, 3, 2, 4]))


########################################################

# def linear_search(nums, target):
#     left, right = 0, len(nums) - 1
#     while left<=right:
#         if target == nums[left]:
#             return left
#         left+=1
# nums = [4, 2, 7, 1, 9]
# target = 7
# print(linear_search(nums, target))

###########################################################

# def binarySearch(nums, target):
#     low = 0
#     high = len(nums) -1
#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] <= target:
#             low = mid+1
#         elif nums[mid] >= target:
#             high = mid-1
#     return -1

# nums= [1,30,5,7,8,40]
# target = 5
# print(binarySearch(nums, target))

###########################################################

def binarySearch(nums, target):
    low = 0
    high = len(nums) -1
    newList=[]
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            newList.append(mid)
            low = mid+1
        elif nums[mid] < target:
            low = mid+1
        elif nums[mid] > target:
            high = mid-1
    return newList

nums= [5, 7, 7, 8, 8, 10]
target = 8
print(binarySearch(nums, target))