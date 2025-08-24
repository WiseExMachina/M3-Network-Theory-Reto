import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Your matrix, defined as a list of lists
adj_matrix_list = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

# --- FIX IS HERE ---
# 1. Convert your list into a proper NumPy array
adj_matrix = np.array(adj_matrix_list)

# 2. Create a graph using the correctly named variable
G = nx.from_numpy_array(adj_matrix)
# --- END FIX ---


# 3. Draw the graph
plt.figure(figsize=(8, 8)) # Made the figure a bit bigger for clarity
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=16, width=2, edge_color='gray', pos=nx.kamada_kawai_layout(G))

# 4. Display the plot
plt.title("Graph from Adjacency Matrix")
plt.show()
