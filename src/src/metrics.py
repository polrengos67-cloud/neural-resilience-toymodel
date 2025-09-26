# src/metrics.py

import numpy as np
import networkx as nx
from typing import Dict, Any

def compute_average_state(states: np.ndarray) -> float:
    """
    Compute the average state of the network.
    
    Args:
        states (np.ndarray): The states of nodes in the network.
    
    Returns:
        float: Average state value.
    """
    return float(np.mean(states))

def compute_state_variance(states: np.ndarray) -> float:
    """
    Compute the variance of the states in the network.
    
    Args:
        states (np.ndarray): The states of nodes in the network.
    
    Returns:
        float: Variance of states.
    """
    return float(np.var(states))

def compute_graph_metrics(graph: nx.Graph) -> Dict[str, Any]:
    """
    Compute various metrics for the network graph.
    
    Args:
        graph (nx.Graph): The network graph.
    
    Returns:
        Dict[str, Any]: Dictionary of metrics.
    """
    metrics = {
        "number_of_nodes": graph.number_of_nodes(),
        "number_of_edges": graph.number_of_edges(),
        "average_clustering": nx.average_clustering(graph),
    }
    return metrics

if __name__ == "__main__":
    # Demo
    from .network import generate_network
    from .dynamics import run_dynamics
    
    network = generate_network()
    final_states = run_dynamics(network)
    
    avg_state = compute_average_state(final_states)
    state_var = compute_state_variance(final_states)
    graph_metrics = compute_graph_metrics(network)
    
    print("Average state:", avg_state)
    print("State variance:", state_var)
    print("Graph metrics:", graph_metrics)
    # TODO: Add more detailed metrics and analyses
