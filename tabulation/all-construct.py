def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if target[i:].startswith(word):
                    table[i + len(word)] += [ suffix + [word] for suffix in table[i]]
    return table[len(target)]


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# []
print(allConstruct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []
