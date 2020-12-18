"""Constants."""
import pickle

DEFAULT_GRAPH = [
    (0, 1, 0.9),
    (0, 2, 0.95),
    (1, 2, 0.8),
    (1, 3, 0.9),
    (3, 1, 0.99),
    (2, 3, 0.85),
]

with open('/home/puff/git-repos/invop/graphs/data/microapple.input', 'rb') as f:
    MICROAPPLE_GRAPH = pickle.load(f)
