import subprocess
import os
import json
from pathlib import Path

def run_graph_to_json():
    try:
        # Specifique path to "graph_to_json.py" relative to main script's emplacement
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Current directory
        graph_to_json_path = os.path.join(script_dir, "All_functions_to_create_graph", "graph_to_json.py")
        
        # Executing the script "graph_to_json.py"
        subprocess.run(["python3", graph_to_json_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running 'graph_to_json.py': {e}")
        return None
    return True

def run_json_to_matAdj_and_txt(graph_number):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Current directory
        json_to_matAdj_and_txt_path = os.path.join(script_dir, "All_functions_to_create_graph", "json_to_matAdj_and_txt.py")
        
        subprocess.run(["python3", json_to_matAdj_and_txt_path, str(graph_number)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running 'json_to_matAdj_and_txt.py': {e}")
        return None
    return True

def run_display_json_to_graph(graph_number):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Current directory
        display_json_to_graph_path = os.path.join(script_dir, "All_functions_to_create_graph", "display_json_to_graph.py")
        
        subprocess.run(["python3", display_json_to_graph_path, str(graph_number)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running 'display_json_to_graph.py': {e}")
        return None
    return True

if __name__ == "__main__":
    print("Creating the graph JSON file...")
    
    if run_graph_to_json():
        print("Graph created successfully!")

        graph_number = input("Enter the number of the graph you want to generate the txt for (e.g., 2 for graph2.json): ")

        if run_json_to_matAdj_and_txt(graph_number):
            print(f"Graph {graph_number} has been successfully converted to text!")

        run_display_json_to_graph(graph_number)