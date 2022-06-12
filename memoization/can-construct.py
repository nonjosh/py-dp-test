def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


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
