#Part 1
def array_count9(nums):
  count = 0
  
  for item in nums:
    if item == 9:
      count = count + 1
  return count

#List-1 > first_last6 
def first_last6(nums):
  if nums[0] == 6:
    return True
  elif nums[len(nums)-1] == 6:
    return True
  else:
    return False

#List-1 > common_end 
def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True

  return False

#List-1 > reverse3 
def reverse3(nums):
  temp = nums[2]
  nums[2] = nums[0]
  nums[0] = temp
  
  return nums

#List-1 > middle_way
def middle_way(a, b):
  lst = [a[1], b[1]]
  return lst

#List-1 > same_first_last 
def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums)-1]:
    return True
  return False
    
#List-1 > sum3 
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

#List-1 > max_end3 
def max_end3(nums):
  if nums[0] < nums[2]:
    temp = nums[2]
    nums[0] = temp
    nums[1] = temp
    return nums
  else:
    temp = nums[0]
    nums[1] = temp
    nums[2] = temp
    return nums

#List-1 > make_ends 
def make_ends(nums):
  if len(nums) == 1:
    lst = [nums[0],nums[0]]
    return lst
  else:
    lst = [nums[0], nums[len(nums)-1]]
    return lst

#List-1 > make_pi 
def make_pi():
  pi = [3, 1, 4]
  return pi

#List-1 > rotate_left3
def rotate_left3(nums):
  temp = nums[0]
  temp2 = nums[1]
  nums[0] = temp2
  nums[1] = nums[2]
  nums[2] = temp
  return nums

#List-1 > sum2
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

#List-1 > has23
def has23(nums):
  for i in range(len(nums)):
    if nums[i] == 2 or nums[i] == 3:
      return True
  return False

#List-2 > count_evens
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count = count + 1
  return count

#List-2 > big_diff 
def big_diff(nums):
  max = nums[0]
  min = nums[0]
  for i in range(len(nums)):
    if nums[i] < min:
      min = nums[i]
    if nums[i] > max:
      max = nums[i]
  return max - min

#List-2 > has22 
def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False

#List-2 > centered_average
def centered_average(nums):
  max = nums[0]
  max_index = 0
  min = nums[0]
  min_index = 0
  avg = 0
  
  for i in range(len(nums)):
    if nums[i] < min:
      min = nums[i]
      min_index = i
    if nums[i] > max:
      max = nums[i]
      max_index = i
    avg = avg + nums[i]
  avg = avg - nums[min_index] - nums[max_index]
  return avg / (len(nums)-2)