def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    result = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            result += countConstruct(suffix, wordBank, memo)
    memo[target] = result
    return result


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
