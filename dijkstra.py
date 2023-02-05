import random

num_nodes = 5
graph = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

for i in range(num_nodes):
    for j in range(i, num_nodes):
        if i != j:
            weight = random.randint(1, 25)
            graph[i][j] = weight
            graph[j][i] = weight

print(graph)