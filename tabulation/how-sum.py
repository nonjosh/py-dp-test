def howSum(targetSum, numbers):
    table = [None for _ in range(targetSum + 2)]
    table[0] = []
    for i in range(0, targetSum):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]
    return table[targetSum]


print(howSum(7, [2, 3]))
# [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))
# [4, 3]
print(howSum(7, [2, 4]))
# None
print(howSum(8, [2, 3, 5]))
# [2, 2, 2, 2]
print(howSum(300, [7, 14]))
# None
