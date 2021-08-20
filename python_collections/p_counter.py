from collections import Counter

# Counter

string_counter = Counter('CollectionsNamedtupleChainMapCounter')
print(sorted(string_counter.elements()))
print(string_counter.most_common(5))

list_counter = Counter([9, 9, 9, 9, 7, 7, 7, 6, 6, 1, 1, 2, 3, 3, 3, 4, 4, 5])
print(sorted(list_counter.elements()))
print(list_counter.most_common(2))
