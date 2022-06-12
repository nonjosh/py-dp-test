def canSum(targetSum, numbers):
    table = [False for _ in range(targetSum + 2)]
    table[0] = True
    for i in range(0, targetSum):
        if table[i]:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True
    return table[targetSum]


print(canSum(7, [2, 3]))
# True
print(canSum(7, [5, 3, 4, 7]))
# True
print(canSum(7, [2, 4]))
# False
print(canSum(8, [2, 3, 5]))
# True
print(canSum(300, [7, 14]))
# False
