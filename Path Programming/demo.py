infinity = float('inf')
# 图使用dict方式存储，层数为起点至终点任意路径节点总数-1
graph = { '4': {'D1': {'E': 5}, 'D2': {'E': 2}},
          '3': {'C1': {'D1': 3, 'D2': 9}, 'C2': {'D1': 6, 'D2': 5}, 'C3': {'D1': 8, 'D2': 10}},
          '2': {'B1': {'C1': 12, 'C2': 14, 'C3': 10}, 'B2': {'C1': 6, 'C2': 10, 'C3': 4}, 'B3': {'C1': 13, 'C2': 12, 'C3': 11}},
          '1': {'A': {'B1': 2, 'B2': 5, 'B3': 1}}}


# 各点到E的最短路径
costs = {'A': infinity,
         'B1': infinity,
         'B2': infinity,
         'B3': infinity,
         'C1': infinity,
         'C2': infinity,
         'C3': infinity,
         'D1': infinity,
         'D2': infinity,
         'E': 0}


# 每个节点最短路径对应父节点
parents = {'A': None,
           'B1': None,
           'B2': None,
           'B3': None,
           'C1': None,
           'C2': None,
           'C3': None,
           'D1': None,
           'D2': None,
           'E': None}


# 动态规划函数
def DP(graph, costs, parents):
    for layer_i in graph.keys():
        for s_node_i in graph[layer_i].keys():
            for d_node_i in graph[layer_i][s_node_i].keys():
                if graph[layer_i][s_node_i][d_node_i] + costs[d_node_i] < costs[s_node_i]:
                    costs[s_node_i] = graph[layer_i][s_node_i][d_node_i] + costs[d_node_i]
                    parents[s_node_i] = d_node_i


# 查找最短路径长度
def find_shortest_path(costs):
    print("The shortest path length is:", costs.get('A'))


# 打印最短路径
def print_shortest_path(parents, startPoint):
    pathStr = startPoint
    startKey = startPoint
    #startValue = parents[startPoint]
    for key, value in parents.items():
        if(value != None):
            if(key == startKey):
                pathStr = pathStr + "->" + value
                startKey = value
            
    print("The shortest path is:", pathStr)

DP(graph, costs, parents)
print(costs)
print(parents)
find_shortest_path(costs)
print_shortest_path(parents, 'A')
