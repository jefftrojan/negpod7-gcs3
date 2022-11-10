# function that takes a list of integer nums and an integer target, and returns indices of the two numbers such that they add up to the target
import random
nums = [2, 4, 1, 3, 5]
target = random.randint(1,9)

def list_parser(nums, target):
    my_dict = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in my_dict:
            return [my_dict[diff], index]
        my_dict[num] = index
    return


output = list_parser(nums, target)
print(output)