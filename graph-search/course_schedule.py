def dfs(graph,vertex,path,order,visited):
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph,neighbor,path,order,visited):
                return False
    # path.remove(vertex)
    order.append(path.pop())
    return True

def cource_schedule(n,prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])

    visited = set()
    path = []
    order = []

    for cource in range(n):
        if cource not in visited:
            visited.add(cource)
            if not dfs(graph,cource,path,order,visited):
                return False
    return True

