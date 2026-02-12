def group_anagrams(words):
    result = []
    visited = [False] * len(words)

    for i in range(len(words)):
        if not visited[i]:
            group = [words[i]]
            visited[i] = True
            for j in range(i + 1, len(words)):
                if not visited[j] and sorted(words[i]) == sorted(words[j]):
                    group.append(words[j])
                    visited[j] = True
            result.append(group)

    return result

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
