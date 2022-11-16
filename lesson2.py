# matrix = [
#     [12, 22, 24, 22, 14],
#     [20, 21, 18, 23, 14],
#     [10, 17, 22, 10, 13],
#     [25, 14, 21, 23, 10],
#     [18, 21, 24, 14, 12]
# ]
#
# for i in range(len(matrix)):
#     print(matrix[i][i], end=' ')


# ls = [1, 2, 3, 4, 5, 6]
# for i in range(1, len(ls) + 1):
#     print(ls[-i], end=' ')


# from math import sqrt
#
# l = lambda x: [i for i in range(1, 101) if not sqrt(i) % 1]
# print(l)

# l1 = [0, 2, 1, 5, 3, 4]
# l = []
#
# for i in range(len(l1)):
#     l.append(l1[l1[i]])
# print(l)


# l = [1, 2, 3, 4]
#
# for i, v in enumerate(l):
#     if i > 0:
#         l[i] += l[i - 1]
# print(l)


# nums = [1, 2, 3, 1, 1, 3]
# c = 0
# for i in range(1, len(nums)):
#     for j in range(i):
#         if nums[i] == nums[j]:
#             c += 1
# print(c)


# nums = [8, 1, 2, 2, 3]
# l = []
# for i in nums:
#     c = 0
#     for j in nums:
#         if j < i:
#             c += 1
#     l.append(c)
# print(l)


# nums = [1, 2, 3, 4]
# res = []
# for i in range(0, len(nums), 2):
#     n = nums[i]
#     for j in range(n):
#         res.append(nums[i + 1])
# print(res)


# s = "codeleet"
# l = [4, 5, 6, 7, 0, 2, 1, 3]
# res = [""] * len(s)
#
# for i, v in zip(l, s):
#     res[i] = v
# print("".join(res))


# nums = [0, 1, 4, 6, 7, 10]
# diff = 3
# c = 0
# for i in range(0, len(nums)):
#     a = nums[i] + diff
#     a1 = a + diff
#     if a in nums and a1 in nums:
#         c += 1
# print(c)


# a = int(input())
#
# if not a % 2:
#     print(a)
# else:
#     print(a * 2)


# nums = [1, 5, 4, 5]
# l = []
# for i in range(len(nums)):
#     for j in range(i):
#         l.append((nums[i] - 1) * (nums[j] - 1))
# print(max(l))


# nums = [-5, 1, 5, 0, -7]
# l = [0]
# s = 0
# for i in range(len(nums)):
#     s += nums[i]
#     l.append(s)
#
# print(max(l))


# nums = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8,
#         2, 3, 4]
#
# s = int(0.05 * len(nums))
#
# while s != 0:
#     nums.remove(max(nums))
#     nums.remove(min(nums))
#     s -= 1
#
# print(sum(nums) / len(nums))


# nums1 = [1, 3]
# nums2 = [2, 7]
# nums3 = nums1 + nums2
# nums3.sort()
# nums_len = len(nums3)
#
# if nums_len == 1:
#     print(nums3[0])
# if nums_len % 2 == 0:
#     print((nums3[nums_len // 2 - 1] + nums3[nums_len // 2]) / 2)
# else:
#     print(nums3[nums_len // 2])


# nums = [2, 7, 11, 15]
# target = 9
# x = {}
# for i in range(len(nums)):
#     c = target - nums[i]
#     if c in x:
#         return [[x[c]], i]
#     x[nums[i]] = i


# nums = [1, 2, 3, 4]
# new = set(nums)
#
# if len(new) == len(nums):
#     print('false')
# print("true")


# nmadur