def fib(num):
    table = [0 for _ in range(num + 2)]
    table[1] = 1
    for i in range(0, num):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[num]

print(fib(6))
# 8
print(fib(7))
# 13
print(fib(8))
# 21
print(fib(50))
# 12586269025
