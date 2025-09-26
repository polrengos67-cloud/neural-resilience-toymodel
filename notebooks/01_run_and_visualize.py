# %%
# # Neural Resilience Toy Model: Run and Visualize

# This notebook demonstrates the functionality of the neural resilience toy model. We will generate a network, run dynamics, compute metrics, and visualize the results.

# %%
# ## Install Dependencies

# Make sure to run this cell to install necessary libraries.
!pip install numpy scipy matplotlib networkx numba

# %%
# ## Import Libraries

import networkx as nx
import numpy as np
from src.network import generate_network
from src.dynamics import run_dynamics
from src.metrics import compute_average_state, compute_state_variance, compute_graph_metrics
from src.utils import plot_network

# %%
# ## Generate Network

n_nodes = 100
p_connect = 0.05
seed = 42

network = generate_network(n_nodes, p_connect, seed)
print("Network generated with", len(network.nodes), "nodes and", len(network.edges), "edges.")

# %%
# ## Run Dynamics

time_steps = 100
final_states = run_dynamics(network, time_steps, seed)
print("Dynamics simulation completed.")

# %%
# ## Compute Metrics

avg_state = compute_average_state(final_states)
state_var = compute_state_variance(final_states)
graph_metrics = compute_graph_metrics(network)

print("Average state:", avg_state)
print("State variance:", state_var)
print("Graph metrics:", graph_metrics)

# %%
# ## Visualize Network

plot_network(network, final_states)
