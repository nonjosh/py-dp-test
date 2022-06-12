def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target)):
        if table[i] > 0:
            for word in wordBank:
                if target[i:].startswith(word):
                    table[i + len(word)] += table[i]
    return table[len(target)]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# 4
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee"],
    )
)
# 0
