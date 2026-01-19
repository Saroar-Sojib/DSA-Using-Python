graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited=[]
def bfs(visited, graph, node):
    queue = []
    res = []
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        res.append(s)
        for x in graph[s]:
            if x not in visited:
                queue.append(x)
                visited.append(x)
    return res 


print(bfs(visited,graph,'A'))


