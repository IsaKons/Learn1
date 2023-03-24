from pprint import pprint

## From pair array to graph
def create_graph(pairs, empty_dict):
    for k, v in pairs:
        empty_dict.setdefault(v, [])
        empty_dict.setdefault(k, []).append(v)
    return empty_dict

empty_dict = {}
pairs = [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('d', 'c'), ('e', 'c'), ('e', 'f')]
graph = [[0,1],[0,2],[1,3],[3,4],[4,5]]
twopart = [[0,1],[0,2],[1,2],[3,4],[4,5]]

create_graph(twopart, empty_dict)

pprint(empty_dict)



# conversion of lists to dictionary
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break

print("Resultant dictionary is : " + str(res))