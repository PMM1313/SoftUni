

def calculate_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calculate_sum(nums, idx + 1)

numbers = [int(x) for x in input().split()]
print(calculate_sum(numbers))