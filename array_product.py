class Solution(object):

    def productExceptSelf(self, nums):

        size = len(nums)
        output = [1] * size

        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left

        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right

        return output
    print(productExceptSelf(0, [1, 2, 6, 8]))
