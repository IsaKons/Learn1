def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            
visited = [] # List to keep track of visited nodes.
# queue is a list that is used to keep track of nodes currently in the queue.
queue = []     #Initialize a queue

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}

dfs(visited, graph, 'A')

bfs(visited, graph, 'A')