import os
import json
import networkx as nx
import matplotlib.pyplot as plt

user_home = os.path.expanduser("~")

graph_number = input("Enter the graph number : ")

json_dir = os.path.join(user_home, "GraphToJsonAndTxtConverter", "graphX_json")

graph_json_path = os.path.join(json_dir, f"graph{graph_number}.json")

if not os.path.exists(graph_json_path):
    print(f"Error: {graph_json_path} does not exist!")
else:
    with open(graph_json_path, 'r') as f:
        data = json.load(f)

G = nx.DiGraph() if data["oriented"] else nx.Graph()

for node_id in data["nodesIds"]:
    node = data[node_id]
    for neighbor, weight in node["adjencyList"]:
        G.add_edge(node_id, neighbor, weight=weight)

pos = {node_id: (data[node_id]["x"], -data[node_id]["y"]) for node_id in data["nodesIds"]}

nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", arrows=bool(data["oriented"]))
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graphe Orienté" if data["oriented"] else "Graphe Non Orienté")
plt.show()
