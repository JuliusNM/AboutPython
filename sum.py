def find_array_quadruplet(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print[[i], nums[i], [j], nums[j]]

        return [i, j]

find_array_quadruplet([4, 7, 8, 5, 4], 9)
