import json
import os

user_home = os.path.expanduser("~")
json_dir = os.path.join(user_home, "GraphToJsonAndTxtConverter", "All_functions_to_create_graph", "graphX_json")
graph_number = input("Enter the graph number you would change with news positions: ")
graph_json_path = os.path.join(json_dir, f"graph{graph_number}.json")

if not os.path.exists(graph_json_path):
    print(f"Error: {graph_json_path} does not exist!")
else:
    with open(graph_json_path, 'r') as f:
        graph = json.load(f)
        
# Définir les colonnes (x) et lignes (y)
x_by_column = {
    120: ["A", "T", "U", "n", "o", "ak", "ai", "az"],
    180: ["B", "S", "V", "m", "p", "ag", "aj", "ay"],
    240: ["C", "R", "W", "l", "q", "af", "ak", "ax"],
    300: ["D", "Q", "X", "k", "r", "ae", "al", "aw"],
    360: ["E", "P", "Y", "j", "s", "ad", "am"],
    420: ["F", "O", "Z", "i", "t", "ac", "an"],
    480: ["G", "N", "a", "h", "u", "ab", "ao", "at"],
    540: ["H", "M", "b", "g", "v", "aa", "ap", "av"],
    600: ["I", "L", "c", "f", "w", "z", "aq", "au"],
    660: ["J", "K", "d", "e", "x", "y", "ar", "as"]
}

y_by_row = {
    125: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    185: ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
    245: ["U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d"],
    305: ["n", "m", "l", "k", "j", "i", "h", "g", "l", "e", "f"],
    365: ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x"],
    425: ["ah", "ag", "af", "ae", "ad", "ac", "ab", "aa", "z", "y"],
    485: ["ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar"],
    545: ["az", "ay", "ax", "aw", "av", "at", "au", "as"]
}

#Creation of a research dictorary
x_lookup = {name: x for x, names in x_by_column.items() for name in names}
y_lookup = {name: y for y, names in y_by_row.items() for name in names}

# Appliquer les coordonnées corrigées
for node in graph["nodesIds"]:
    if node in graph:
        if node in x_lookup:
            graph[node]["x"] = x_lookup[node]
        if node in y_lookup:
            graph[node]["y"] = y_lookup[node]

# Sauvegarder le résultat dans un nouveau fichier
with open(f"graph{graph_number}_corrected.json", "w") as f:
    json.dump(graph, f, indent=4)

print(f"Coordinates of graph{graph_number}. json have been changed and saved in the file graph{graph_number}_corrected.json ✅")
