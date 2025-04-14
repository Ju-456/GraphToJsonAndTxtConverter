import json
import numpy as np
import os

user_home = os.path.expanduser("~")

graph_number = input("Enter the graph number : ")

json_dir = os.path.join(user_home, "GraphToJsonAndTxtConverter", "All_functions_to_create_graph", "graphX_json")
txt_dir = os.path.join(user_home, "GraphToJsonAndTxtConverter", "All_functions_to_create_graph","graphX_txt")

graph_json_path = os.path.join(json_dir, f"graph{graph_number}.json")

if not os.path.exists(graph_json_path):
    print(f"Error: {graph_json_path} does not exist!")
else:
    with open(graph_json_path, 'r') as f:
        data = json.load(f)

    nodes = data["nodesIds"]
    node_indices = {node: idx for idx, node in enumerate(nodes)}
    n = len(nodes)
    adj_matrix = np.zeros((n, n), dtype=int)

    for node in nodes:
        for neighbor, weight in data[node]["adjencyList"]:
            i = node_indices[node]
            j = node_indices[neighbor]
            adj_matrix[i][j] = weight

    col_width = 4  # display with good widght
    header = " " * (col_width + 1) + "".join(f"{node:>{col_width}}" for node in nodes)
    print("Weighted adjacency matrix :")
    print(header)
    for i, row in enumerate(adj_matrix):
        row_str = "".join(f"{val:>{col_width}}" for val in row)
        print(f"{nodes[i]:<{col_width}} {row_str}")

    os.makedirs(txt_dir, exist_ok=True)

    i = 1
    while os.path.exists(os.path.join(txt_dir, f"graph{graph_number}.txt")):
        i += 1

    txt_file_path = os.path.join(txt_dir, f"graph{graph_number}.txt")

    with open(txt_file_path, "w") as f:
        for row in adj_matrix:
            f.write(" ".join(map(str, row)) + "\n")

    print(f"\nYou can find {txt_file_path} in the folder grapheX_txt")
