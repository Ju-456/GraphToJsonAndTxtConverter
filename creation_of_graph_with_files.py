import subprocess
import os
import json
from pathlib import Path
import re

def run_graph_to_json():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        graph_to_json_path = os.path.join(script_dir, "All_functions_to_create_graph", "graph_to_json.py")
        
        result = subprocess.run(
            ["python3", graph_to_json_path],
            check=True,
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr  # fusion of stdout + stderr
        print("Output from graph_to_json.py:")
        print(output)

        # Match: graph<number>.json
        match = re.search(r"graph(\d+)\.json", result.stdout)
        if match:
            return match.group(1)
        else:
            print("Could not find graph number in the output.")
            return None

    except subprocess.CalledProcessError as e:
        print(f"Error while running 'graph_to_json.py': {e}")
        return None
    
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

    graph_number = run_graph_to_json()  

    if graph_number:
        print(f"Graph n°{graph_number} created successfully!")

        if run_json_to_matAdj_and_txt(graph_number):
            print(f"Graph {graph_number} has been successfully converted to text!")

        run_display_json_to_graph(graph_number)
    else:
        print("Graph creation failed.")
