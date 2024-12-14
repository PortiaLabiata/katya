from operator import itemgetter
n = int(input())
nums = dict()
for i in range(0, n):
    x = int(input())
    if x not in nums.keys(): nums[x] = 1
    else: nums[x] += 1

print(max(nums.items(), key=itemgetter(1))[0])
