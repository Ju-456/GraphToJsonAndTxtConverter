import os
import json
import networkx as nx
import tkinter as tk
import math

user_home = os.path.expanduser("~")

graph_number = input("Enter the graph number : ")

json_dir = os.path.join(user_home, "GraphToJsonAndTxtConverter", "All_functions_to_create_graph", "graphX_json")

graph_json_path = os.path.join(json_dir, f"graph{graph_number}.json")

if not os.path.exists(graph_json_path):
    print(f"Error: {graph_json_path} does not exist!")
else:
    try:
        with open(graph_json_path, 'r') as f:
            data = json.load(f)

        if "oriented" in data:
            G = nx.DiGraph() if data["oriented"] else nx.Graph()
        else:
            print("Warning: 'oriented' key not found in the data. Defaulting to undirected graph.")
            G = nx.Graph() # Use a Non-oriented graph if the key "orienteed" isn't here 

        for node_id in data["nodesIds"]:
            node = data[node_id]
            for neighbor, weight in node["adjencyList"]:
                G.add_edge(node_id, neighbor, weight=weight)

        pos = {node_id: (data[node_id]["x"], data[node_id]["y"]) for node_id in data["nodesIds"]}

        root = tk.Tk()
        canvas = tk.Canvas(root, width=800, height=600, bg="#d0ecff")
        canvas.pack()

        def draw_edge(n1, n2, weight):
            x1, y1 = pos[n1]
            x2, y2 = pos[n2]

            dx = x2 - x1
            dy = y2 - y1
            dist = math.hypot(dx, dy)
            if dist == 0:
                return

            offset = 18
            x1b = x1 + dx * offset / dist
            y1b = y1 + dy * offset / dist
            x2b = x2 - dx * offset / dist
            y2b = y2 - dy * offset / dist

            canvas.create_line(
                x1b, y1b, x2b, y2b,
                fill="black",
                arrow=tk.LAST,
                arrowshape=(12, 15, 5),
                width=1.5
            )

            mx, my = (x1b + x2b) / 2 + 10, (y1b + y2b) / 2 - 10
            canvas.create_text(mx, my, text=str(weight), fill="#38b6ff", font=("Helvetica", 10))

        for node_id in data["nodesIds"]:
            x, y = pos[node_id]
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="#163180")
            canvas.create_text(x, y, text=node_id, fill="white", font=("Helvetica", 12))

        for n1, n2, data in G.edges(data=True):
            draw_edge(n1, n2, data["weight"])

        canvas.create_text(400, 30, text="Hopefully the graph is correct!", fill="black", font=("Helvetica", 12))

        root.mainloop()

    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {graph_json_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")
