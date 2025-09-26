# src/dynamics.py

import numpy as np
import networkx as nx
from typing import Dict, Any

def initialize_states(graph: nx.Graph, seed: int = 42) -> np.ndarray:
    """
    Initialize the state of each node in the network.
    
    Args:
        graph (nx.Graph): The network with nodes to initialize states for.
        seed (int): Seed for random number generator.
    
    Returns:
        np.ndarray: Array of initial states.
    """
    rng = np.random.default_rng(seed)
    states = rng.random(len(graph.nodes))
    return states

def update_states(graph: nx.Graph, states: np.ndarray, time_steps: int = 100, seed: int = 42) -> np.ndarray:
    """
    Update the state of the network over a number of time steps.
    
    Args:
        graph (nx.Graph): The network with nodes to update states.
        states (np.ndarray): Current states of the nodes.
        time_steps (int): Number of time steps to simulate.
        seed (int): Seed for random processes.
    
    Returns:
        np.ndarray: States after the time steps.
    """
    rng = np.random.default_rng(seed)
    for _ in range(time_steps):
        new_states = states.copy()
        for node in graph.nodes:
            influence = sum(graph.edges[node, neighbor]['weight'] * states[neighbor] for neighbor in graph.neighbors(node))
            new_states[node] = np.tanh(influence)
        states = new_states + rng.normal(0, 0.01, size=states.shape)  # add noise
    return states

def run_dynamics(graph: nx.Graph, time_steps: int = 100, seed: int = 42) -> np.ndarray:
    """
    Run the entire simulation of dynamics on the network.
    
    Args:
        graph (nx.Graph): The network to simulate on.
        time_steps (int): Number of time steps to simulate.
        seed (int): Seed for random processes.
    
    Returns:
        np.ndarray: Final states of the nodes.
    """
    states = initialize_states(graph, seed)
    final_states = update_states(graph, states, time_steps, seed)
    return final_states

if __name__ == "__main__":
    # Demo
    from .network import generate_network
    network = generate_network()
    final_states = run_dynamics(network)
    print("Final states:", final_states[:10])  # Print first 10 states for brevity
    # TODO: Integrate metrics for state analysis
