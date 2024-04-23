# def merge(nums1: list, m: int, nums2: list, n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     nums2.reverse()
#     nums1[m:] = nums2
#     nums1.sort()
#     print(nums1)
#
#
# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([-1,0,0,3,3,3,0,0,0], 6, [1, 2, 3], 3)


# def removeElement(nums: list, val: int) -> int:
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] == val:
#             nums[i] = None
#         else:
#             k += 1
#
#     nums.sort(key=lambda x: x is None)
#     return k
#
#
# print(removeElement([3, 2, 2, 3], 3))


# def removeDuplicates(nums: list) -> int:
#     k = 0
#     for i in range(len(set(nums))):
#         if nums.count(nums[i]) > 1:
#             nums[i] = None
#         else:
#             k += 1
#     nums.sort(key=lambda x: x is None)
#     return k
#
# removeDuplicates([1, 1, 2])


# def removeDuplicates(nums: list) -> int:
#     k = 0
#     for i in range(len(nums)):
#         if nums.count(nums[i]) > 2:
#             nums[i] = None
#         else:
#             k += 1
#     nums.sort(key=lambda x: x is None)
#     return k
#
#
# removeDuplicates([1, 1, 1, 2, 2, 3])


# def majorityElement(nums: list) -> int:
#     # for i in range(len(nums)):
#     #     if nums.count(nums[i]) > len(nums) / 2:
#     #         return nums[i]
#
#     return next(i for i in set(nums) if nums.count(i) > len(nums) / 2)
#
#
# print(majorityElement([3, 2, 3]))
# print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


# def rotate(nums: list, k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     # nums[:] = nums[-k:] + nums[:-k] if len(nums) > k else nums[::-1]
#     # lol = map(lambda x: nums.insert(0, nums.pop()), range(k))
#     for _ in range(k):
#         nums.insert(0, nums.pop())
#     print(nums)
#
#
# rotate([1, 2, 3, 4, 5, 6, 7], 3)
# rotate([1, 2], 3)

# def maxProfit(prices: list) -> int:
# profit = 0
# for i in range(0, len(prices) - 1):
#     max_p = max(prices[i + 1:])
#     if prices[i] < max_p:
#         temp_profit = max_p - prices[i]
#         profit = temp_profit if profit < temp_profit else profit
#     if profit > max_p:
#         break
# return profit

# profit = 0
# while len(prices) > 0:
#     max_p = max(set(prices))
#     if prices[0] < max_p:
#         temp_profit = max_p - prices[0]
#         profit = temp_profit if profit < temp_profit else profit
#     prices[:] = prices[1:]
# return profit

# profit = 0
# lenPrice = len(prices)
# for i in range(0, lenPrice):
#     prices[:] = prices[i + 1:]
#     print(prices, profit)
#     if len(prices) < 3:
#         break
#     max_price = max(prices)
#     if prices[i] < max_price:
#         temp_profit = max_price - prices[i]
#         profit = temp_profit if profit < temp_profit else profit
# print(profit)
# return profit


# maxProfit([7, 1, 5, 3, 6, 4])
# maxProfit([7, 6, 4, 3, 1])
# maxProfit([2, 1, 4])


# def maxProfit(prices: list) -> int:
#     profit = 0
#     buy = prices[0]
#     for sell in prices[1:]:
#         if sell > buy:
#             print(profit, buy, sell)
#             profit += sell - buy
#         buy = sell
#     return profit
#
#
# maxProfit([7, 1, 5, 3, 6, 4])
# # maxProfit([7, 6, 4, 3, 1])
# # maxProfit([2, 1, 4])


# def canJump(nums: list) -> bool:
#     jump = nums[1]
#     curr_index = 1
#     all_len = len(nums) - 1
#
#     for i in range(len(nums)):
#         if curr_index == all_len:
#             break
#         if i == curr_index:
#             nums[:] = nums[nums[jump]:]
#             print(jump)
#             jump = nums[0]
#             curr_index += jump
#
#     # print(nums, jump, curr_index, all_len)
#     return curr_index == all_len
#
# # print(canJump([2, 3, 1, 1, 4]))
# # print('-----------------')
# print(canJump([3, 2, 1, 0, 4]))

# def romanToInt(s: str) -> int:
#     roman_num = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     return sum(roman_num[r] for r in s[::-1])
#
# print(romanToInt("III"))
# print(romanToInt("MCMXCIV"))

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A7 = [i % 2 and i for i in A1 if 2 < i < 8]
print(A7)

print(','.join(str(j**2) for j in range(10)))
