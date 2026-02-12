def groupedanagrams(words):
    grouped={}

    for word in words:
         key ="".join(sorted(word))
         print(key)

         if key not in grouped:
             grouped[key] = [word]
         else:
            grouped[key].append(word)

    return grouped

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupedanagrams(words))