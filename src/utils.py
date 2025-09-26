# src/utils.py

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def plot_network(graph: nx.Graph, states: np.ndarray) -> None:
    """
    Plot the network with node states.
    
    Args:
        graph (nx.Graph): The network graph to plot.
        states (np.ndarray): Node states to reflect in node color.
    """
    pos = nx.spring_layout(graph, seed=42)  # Position nodes for consistent layout
    node_colors = plt.cm.viridis(states)  # Color nodes by state using a colormap
    nx.draw(graph, pos, node_color=node_colors, with_labels=True, node_size=300, edge_color='gray')
    plt.title("Network visualization with node states")
    plt.show()

def save_plot(name: str) -> None:
    """
    Save the current plot to a file.
    
    Args:
        name (str): Filename to save the plot to.
    """
    plt.savefig(name, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Demo
    from .network import generate_network
    from .dynamics import initialize_states
    
    network = generate_network()
    initial_states = initialize_states(network)
    
    plot_network(network, initial_states)
    save_plot("network_plot.png")
    print("Network plot saved as 'network_plot.png'.")
    # TODO: Implement more visualization options
