import tkinter as tk
from tkinter.simpledialog import askstring
import json
import math
import os

class GraphBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Directed Graph Builder")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="#d0ecff")  # light blue
        self.canvas.pack()

        self.nodes = {}  # name -> (x, y)
        self.node_history = []  # Stack of added node names (to remove if we need)
        self.root.bind("<Control-z>", self.undo_last_action)  # Undo node or edge
    
        self.edges = []  # (source, target, weight)
        self.edge_history = []  # Keep track of edges
        self.root.bind("<Control-Shift-z>", self.undo_last_edge)  # Undo edge

        self.node_count = 0
        self.selected_node = None

        self.canvas.bind("<Button-1>", self.add_or_select_node)

        export_btn = tk.Button(root, text="Export to JSON", command=self.export_json)
        export_btn.pack()
        
    def get_next_node_name(self):
        index = self.node_count
        name = ''
        while True:
            if index < 26:
                name = chr(65 + index)  # A-Z
            elif index < 52:
                name = chr(97 + index - 26)  # a-z
            else:
                # Génère des noms comme aa, ab, ac, ..., ba, bb, etc.
                base = index - 52
                name = ''
                while base >= 0:
                    name = chr(97 + (base % 26)) + name
                    base = base // 26 - 1
            return name
    def add_or_select_node(self, event):
        clicked_node = self.get_node_at_position(event.x, event.y)
        if clicked_node:
            if self.selected_node and self.selected_node != clicked_node:
                weight = askstring("Edge Weight", f"Weight from {self.selected_node} to {clicked_node}:")
                if weight is not None:
                    try:
                        weight = int(weight)
                        self.edges.append((self.selected_node, clicked_node, weight))
                        self.draw_edge(self.selected_node, clicked_node, weight)
                        self.node_history.append(self.selected_node)  # Keep track of selected node
                        self.edge_history.append((self.selected_node, clicked_node, weight))  # Keep track of the edge
                    except ValueError:
                        pass
                    self.selected_node = None
            else:
                self.selected_node = clicked_node
        else:
            name = self.get_next_node_name()
            self.nodes[name] = (event.x, event.y)
            self.node_count += 1
            self.node_history.append(name)  # Add new node to history
            self.draw_node(name, event.x, event.y)

    def undo_last_action(self, event=None):
        """Undo the last added action (either node or edge)."""
        if not self.node_history and not self.edge_history:
            return

        if self.edge_history:
            # Undo the last edge
            last_edge = self.edge_history.pop()  # Get the last edge added
            self.edges = [e for e in self.edges if e != last_edge]  # Remove the edge from the graph

            # Redraw everything after removing the edge
            self.canvas.delete("all")
            for name, (x, y) in self.nodes.items():
                self.draw_node(name, x, y)
            for src, tgt, w in self.edges:
                self.draw_edge(src, tgt, w)
        elif self.node_history:
            # If there is no edge history to undo, undo the node history (remove node)
            last_node = self.node_history.pop()  # Get the last node added
            del self.nodes[last_node]  # Remove the node from the graph

            # Remove associated edges
            self.edges = [e for e in self.edges if e[0] != last_node and e[1] != last_node]

            # Reset node count if we remove a node, so the next one is named correctly
            self.node_count = ord(last_node) - 65  # Recalculate the node count

            # Redraw everything
            self.canvas.delete("all")
            for name, (x, y) in self.nodes.items():
                self.draw_node(name, x, y)
            for src, tgt, w in self.edges:
                self.draw_edge(src, tgt, w)

    def undo_last_edge(self, event=None):
        """Undo the last added edge."""
        if not self.edge_history:
            return

        last_edge = self.edge_history.pop()  # Get the last edge added
        self.edges = [e for e in self.edges if e != last_edge]  # Remove the edge from the graph

        # Redraw everything after removing the edge
        self.canvas.delete("all")
        for name, (x, y) in self.nodes.items():
            self.draw_node(name, x, y)
        for src, tgt, w in self.edges:
            self.draw_edge(src, tgt, w)

    def get_node_at_position(self, x, y, radius=15):
        """Get the node at a specific position on the canvas."""
        for name, (nx, ny) in self.nodes.items():
            if (x - nx)**2 + (y - ny)**2 <= radius**2:
                return name
        return None

    def draw_node(self, name, x, y):
        """Draw a node on the canvas."""
        r = 15
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#163180", outline="#163180")
        self.canvas.create_text(x, y, text=name, fill="white")

    def draw_edge(self, n1, n2, weight):
        """Draw an edge between two nodes on the canvas."""
        x1, y1 = self.nodes[n1]
        x2, y2 = self.nodes[n2]

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

        self.canvas.create_line(
            x1b, y1b, x2b, y2b,
            fill="black",
            arrow=tk.LAST,
            arrowshape=(12, 15, 5),
            width=1.5
        )

        mx, my = (x1b + x2b) / 2 + 10, (y1b + y2b) / 2 - 10
        self.canvas.create_text(mx, my, text=str(weight), fill="#38b6ff", font=("Helvetica", 10, "bold"))

    def export_json(self):
        """Export the graph to a JSON file."""
        graph_data = {
            "oriented": 1,
            "nodesIds": list(self.nodes.keys())
        }

        # Add node details with coordinates and adjacency list
        for node in self.nodes:
            x, y = self.nodes[node]
            adjacency_list = [
                [target, weight]
                for (src, target, weight) in self.edges
                if src == node
            ]
            graph_data[node] = {
                "x": x,
                "y": y,
                "adjencyList": adjacency_list
            }

        # Define the output directory
        base_path = os.path.dirname(os.path.abspath(__file__))
        target_dir = os.path.join(base_path, "graphX_json")
        os.makedirs(target_dir, exist_ok=True)

        # Find the next available file name
        i = 1
        while os.path.exists(os.path.join(target_dir, f"graph{i}.json")):
            i += 1

        filename = os.path.join(target_dir, f"graph{i}.json")

        # Write the JSON to file
        with open(filename, "w") as f:
            json.dump(graph_data, f, indent=4)

        print(f"\nGraph saved to {filename}")

        # Show the result in a new popup window
        export_window = tk.Toplevel(self.root)
        export_window.title("Exported JSON")
        text = tk.Text(export_window, wrap="word")
        with open(filename, "r") as f:
            text.insert("1.0", f.read())
        text.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphBuilder(root)
    root.mainloop()
