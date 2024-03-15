import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for illustration
np.random.seed(42)
num_cells = 10

# Create a random graph
G = nx.gnp_random_graph(num_cells, p=0.3)

# Assign random sizes and colors to nodes
node_sizes = np.random.uniform(50, 200, num_cells)
node_colors = np.random.rand(num_cells)

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the graph with nodes colored by size and color
nx.draw(G, pos=nx.spring_layout(G), ax=ax, node_size=node_sizes, node_color=node_colors, cmap='viridis')

# Add colorbar
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=ax)
cbar.set_label('Node Color')

# Set title
ax.set_title('Cancer Cell Network Graph')

# Display the plot
plt.show()
