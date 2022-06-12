def canConstruct(target, wordBank):
    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if target[i:].startswith(word):
                    table[i + len(word)] = True
    return table[len(target)]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# True
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee"],
    )
)
# False
