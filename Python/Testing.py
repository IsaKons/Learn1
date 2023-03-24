def create_graph(pairs, empty_dict):
    for k, v in pairs:
        empty_dict.setdefault(v, [])
        empty_dict.setdefault(k, []).append(v)
    return empty_dict

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            
n = 6
array1 = [[0,1],[0,2],[1,3],[3,4],[4,5]]
array2 = [[0,1],[0,2],[1,2],[3,4],[4,5]]

graph = {}
graph = create_graph(array1, graph)

visited = 0
buffer = []
for x in range(n):
    if x not in buffer:
        buffer2 = dfs(buffer, graph, x)
        buffer.append(buffer2)
        visited += 1

print(visited)
        
