from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
    def __init__(self):
        self.visual = []
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

# Driver code
G = GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(7, 7)
G.visualize()

def create_graph(pairs, empty_dict):
    for k, v in pairs:
        empty_dict.setdefault(v, []).append(k)
        empty_dict.setdefault(k, []).append(v)
    return empty_dict

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
    return visited

def dfs_recursive(graph, source,path = []):  
       if source not in path:  
           path.append(source)  
           if source not in graph:   
               return path  
           for neighbour in graph[source]:  
               path = dfs_recursive(graph, neighbour, path)  
       return path
   
def dfs2(visited, graph, start):
    visited.append(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

n = 100
sectors = 0
alone = 0
buffer = []
graph = {}
visited = []
path = []

array1 = [[0,1],[0,2],[1,3],[3,4],[4,5]]
array2 = [[0,1],[0,2],[1,2],[3,4],[4,5]]
array3 = [[17,51],[33,83],[53,62],[25,34],[35,90],[29,41],[14,53],[40,84],[41,64],[13,68],[44,85],[57,58],[50,74],[20,69],[15,62],[25,88],[4,56],[37,39],[30,62],[69,79],[33,85],[24,83],[35,77],[2,73],[6,28],[46,98],[11,82],[29,72],[67,71],[12,49],[42,56],[56,65],[40,70],[24,64],[29,51],[20,27],[45,88],[58,92],[60,99],[33,46],[19,69],[33,89],[54,82],[16,50],[35,73],[19,45],[19,72],[1,79],[27,80],[22,41],[52,61],[50,85],[27,45],[4,84],[11,96],[0,99],[29,94],[9,19],[66,99],[20,39],[16,85],[12,27],[16,67],[61,80],[67,83],[16,17],[24,27],[16,25],[41,79],[51,95],[46,47],[27,51],[31,44],[0,69],[61,63],[33,95],[17,88],[70,87],[40,42],[21,42],[67,77],[33,65],[3,25],[39,83],[34,40],[15,79],[30,90],[58,95],[45,56],[37,48],[24,91],[31,93],[83,90],[17,86],[61,65],[15,48],[34,56],[12,26],[39,98],[1,48],[21,76],[72,96],[30,69],[46,80],[6,29],[29,81],[22,77],[85,90],[79,83],[6,26],[33,57],[3,65],[63,84],[77,94],[26,90],[64,77],[0,3],[27,97],[66,89],[18,77],[27,43]]

graph = create_graph(array3, graph)
node = 1
dfs2(visited, graph, node)
dfs(visited, graph, node)
dfs_recursive(graph, node)
pprint(graph)

for x in range(n):
    if x not in buffer:
        if x in graph:
            visited = []
            buffer += dfs(visited, graph, 0)
            sectors += 1
        else:
            buffer.append(x)
            alone += 1

print(alone)
print(sectors)
print(buffer)

if bool(graph[28]):
    print("None")

for x in graph:
    if bool(graph[x]):
        for y in graph[x]:
            G.addEdge(x, y)
        
G.visualize()