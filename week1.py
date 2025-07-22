graph ={}
edge_set=set()

#Addnode only if it doesn't already exist
def addnode(node):
    if node in graph:
        print(f"'{node}' already exists.please enter a different node.")
        return false
    graph[node]=[]
    return True
#add edge only if not a duplicate
def addedge(u,v):
    edge=tuple(sorted((u,v)))
    if edge in edge_set:
        printf(f"'edge {u}-{v} alreday exists please enter adifferent edge")
        return False
    if u not in graph or v not in graph:
        print("both nodes must be added before connecting them with an edge")
        return false
    graph[u].append(v)
    graph[v].append(u)
    edge_set.add(edge)
    return True
#BFS
def bfs(start):
    visited=[]
    queue=[start]
    print("BFS:",end="")
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node,end="")
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

#DFS
def dfs(node,visited=None):
    if visited is None:
        visited=[]
        print("DFS:",end="")
    if node not in visited:
        print(node,end="")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor,visited)
#===Input Section===
#Add unique nodes
n=int(input("enter number of nodes:"))
i=0
while i<n:
    node=input(f"enter node{i+1}:").strip()
    if addnode(node):
        i+=1
#Add edges without duplication
e=int(input("Enter number of edges:"))
for i in range(e):
    while True:
        u,v=input(f"Enter edge {i+1} (two nodes):").split()
        if addedge(u,v):
            break
#strat traversal
start =input("enter starting node:").strip()
if start in graph:
    bfs(start)
    dfs(start)
    print()
else:
    print("Starting node not found in the graph.")
        
