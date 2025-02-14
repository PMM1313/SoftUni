def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):
           if nums[curr_idx] < nums[min_idx]:
               min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
    pass

numbers = [int(x) for x in input().split()]
selection_sort(numbers)
print(*numbers)