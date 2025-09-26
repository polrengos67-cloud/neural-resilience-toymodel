# tests/test_simulator.py

import pytest
import networkx as nx
from src.network import generate_network
from src.dynamics import run_dynamics
from src.metrics import compute_average_state, compute_state_variance

def test_generate_network():
    network = generate_network(10, 0.2, seed=42)
    assert len(network.nodes) == 10
    assert 0 <= len(network.edges) <= 45  # Max possible edges C(10,2)

def test_run_dynamics():
    network = generate_network(10, 0.2, seed=42)
    final_states = run_dynamics(network, time_steps=10, seed=42)
    assert len(final_states) == 10

def test_metrics():
    states = [0.2, 0.4, 0.6, 0.8]
    avg_state = compute_average_state(states)
    assert avg_state == pytest.approx(0.5, rel=1e-2)

    state_var = compute_state_variance(states)
    assert state_var == pytest.approx(0.05, rel=1e-2)
