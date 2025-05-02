# 🔁 Directed Graph Converter

## 🌟 Project Goal

This project is designed to **convert directed graphs** into a **weighted adjacency matrix** in `.txt` format.  
It also provides modular tools for other purposes such as visualization, JSON generation, and more.

---

## 🚀 How It Works

Run the main script:

```bash
python3 creation_of_graph_with_files.py
```

It will automatically execute the following steps in order:

1. **graph_to_json** – Build a directed graph (via GUI) and export it as a `.json` file.
2. **json_to_matAdj_and_txt** – Convert the `.json` into a `.txt` file representing the **weighted adjacency matrix**.
3. **display_json_to_graph** – Visualize the graph to ensure that everything is correct.

---

## 🔧 Modular Design

Each step is modular and can be used independently, depending on your use case.  
All functionalities are located in the `All_functions_to_create_graph` folder.

### Available Tools:

- ➔ `graph_to_json.py`  
  Create a directed graph and export it as a `.json`.

- ➔ `json_to_matAdj_and_txt.py`  
  Convert a `.json` file into a `.txt` file with the weighted adjacency matrix.

- ➔ `display_json_to_graph.py`  
  Display any directed graph defined in a `.json` file for easy verification.

- ➔ `normalize_json_graph_positions.py` (new 🌟)  
  Adjust node/vertex positions in a `.json` graph for cleaner, straighter visual displays.

---

## 💡 Why This Project?

Originally built to support the *NaturalDisasterManagementSystem*, this project aims to **simplify the creation and manipulation of directed graphs**. It provides tools to:
- Quickly simulate and visualize graphs  
- Generate both JSON (for graphical use) and adjacency matrices (for algorithmic use)  
- Keep graph workflows clean, modular, and extensible

---

## 📁 Project Structure

```
GraphToJsonAndTxtConverter/
├── creation_of_graph_with_files.py        # Main script (calls everything)
├── All_functions_to_create_graph/
│   ├── graph_to_json.py                   # Create graph ➔ JSON
│   ├── json_to_matAdj_and_txt.py         # JSON ➔ TXT matrix
│   ├── display_json_to_graph.py          # JSON ➔ Graph display
│   ├── graphX_json/                       # Stores generated JSON files
│   ├── graphX_txt/                        # Stores TXT adjacency matrices
```

---

## ✅ Example Usage

```bash
$ python3 creation_of_graph_with_files.py
Creating the graph JSON file...
Graph created successfully!
Enter the number of the graph you want to generate the txt for (e.g., 2 for graph2.json): 3
Weighted adjacency matrix:
    A   B   C
A   0   5   0
B   0   0   1
C   2   0   0
Graph 3 has been successfully converted to text!
(Then, the graph is displayed for verification)
```

---
🚧 More tweaks and improvements coming soon!

Feel free to contact me for any question !


