# src/network.py

import networkx as nx
import numpy as np
from typing import Tuple

def create_random_network(n_nodes: int, p_connect: float, seed: int = 42) -> nx.Graph:
    """
    Create a random graph with n_nodes and connection probability p_connect.
    
    Args:
        n_nodes (int): Number of nodes in the network.
        p_connect (float): Probability of connection between nodes.
        seed (int): Seed for random number generator.

    Returns:
        nx.Graph: Generated random graph.
    """
    rng = np.random.default_rng(seed)
    graph = nx.erdos_renyi_graph(n_nodes, p_connect, seed=seed)
    return graph

def add_weights_to_network(graph: nx.Graph, weight_range: Tuple[float, float] = (0.1, 1.0), seed: int = 42) -> None:
    """
    Add weights to the edges of the network.
    
    Args:
        graph (nx.Graph): The network to add weights to.
        weight_range (Tuple[float, float]): The range of weights.
        seed (int): Seed for random number generator.
    """
    rng = np.random.default_rng(seed)
    for u, v in graph.edges():
        graph.edges[u, v]['weight'] = rng.uniform(*weight_range)

def generate_network(n_nodes: int = 100, p_connect: float = 0.05, seed: int = 42) -> nx.Graph:
    """
    Generate a random weighted network.
    
    Args:
        n_nodes (int): Number of nodes in the network.
        p_connect (float): Probability of connection between nodes.
        seed (int): Seed for random number generator.
    
    Returns:
        nx.Graph: A random weighted network.
    """
    graph = create_random_network(n_nodes, p_connect, seed)
    add_weights_to_network(graph, seed=seed)
    return graph

if __name__ == "__main__":
    # Demo
    network = generate_network()
    print("Generated network with", len(network.nodes), "nodes and", len(network.edges), "edges.")
    # TODO: Add visualization and detailed metrics
