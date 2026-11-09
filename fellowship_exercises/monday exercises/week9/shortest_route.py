#Week 9 
#Question E3

def shortest_path(graph, start, goal):
    res = []
    # visited = {}
    if start == goal:
        return [start]

    if graph[start] == []:
        return res
    
    temp = start
    i = 0
    while True:
        vals = graph[temp]
        
        if vals[i] not in res:
            res.append(temp)
            temp = vals[i]

        if temp == goal:
            res.append(temp)
            return res

def reachable(graph, start):
    visited = {}
    temp = start
    route = [start]
    while True:
        vals = graph[temp]
        for item in vals:
            road = route.copy()
            road.append(item)
            visited[item] = road
            



 






graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}


print(shortest_path(graph, "C", "F"))


