"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""


def main():
    test = [(7, 9), (2, 4), (5, 7)]
    intervals(test)


def intervals(vals):
    nums = {}

    #populate dict
    for i in range(len(vals)):
        val = vals[i]
        update_dict(nums, val, i)

    for i in range(min(nums), max(nums)+1):
        if len(nums[i]) != 0 & len(nums[i]) != 1:
            #check if overlap or just touching
            for j in range






def update_dict(nums: dict, interval: tuple, intervalIndex: int):
    """
    @param nums:
    @param interval:
    @param intervalIndex:
    """
    for i in range(interval[0], interval[1]+1):
        if i not in nums:
            nums[i] = (intervalIndex,)
        else:
            nums[i] = nums[i] + (intervalIndex,)
    print(nums)


if __name__ == "__main__":
    main()
