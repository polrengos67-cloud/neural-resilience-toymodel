# scripts/run_experiment.py

from src.network import generate_network
from src.dynamics import run_dynamics
from src.metrics import compute_average_state, compute_state_variance, compute_graph_metrics
from src.utils import plot_network, save_plot

def run_experiment(n_nodes: int = 100, p_connect: float = 0.05, time_steps: int = 100, seed: int = 42) -> None:
    """
    Run a complete experiment with network generation, dynamics simulation, and result visualization.
    
    Args:
        n_nodes (int): Number of nodes in the network.
        p_connect (float): Probability of connection between nodes.
        time_steps (int): Number of time steps for dynamics simulation.
        seed (int): Seed for reproducibility.
    """
    # Step 1: Generate network
    network = generate_network(n_nodes, p_connect, seed)
    
    # Step 2: Simulate dynamics
    final_states = run_dynamics(network, time_steps, seed)
    
    # Step 3: Compute metrics
    avg_state = compute_average_state(final_states)
    state_var = compute_state_variance(final_states)
    graph_metrics = compute_graph_metrics(network)
    
    # Step 4: Display results
    print("Average state:", avg_state)
    print("State variance:", state_var)
    print("Graph metrics:", graph_metrics)
    
    # Step 5: Visualize network
    plot_network(network, final_states)
    save_plot("experiment_plot.png")
    print("Experiment completed and plot saved as 'experiment_plot.png'.")

if __name__ == "__main__":
    run_experiment()
    # TODO: Add command-line arguments and additional experiment configurations
