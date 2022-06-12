def bestSum(targetSum, numbers):
    table = [None for _ in range(targetSum + 2)]
    table[0] = []
    for i in range(0, targetSum):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = table[i] + [num]
                    # if this combination is the shortest, update the table
                    if table[i + num] is None or len(combination) < len(table[i + num]):
                        table[i + num] = combination
    return table[targetSum]


print(bestSum(7, [5, 3, 4, 7]))
# [7]
print(bestSum(8, [2, 3, 5]))
# [5, 3]
print(bestSum(8, [1, 4, 5]))
# [4, 4]
print(bestSum(100, [1, 2, 5, 25]))
# [25, 25, 25, 25]
