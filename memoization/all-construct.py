def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = [[word] + suffixWay for suffixWay in suffixWays]
            result.extend(targetWays)

    memo[target] = result
    return result

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# []
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []
