# Directed Graph Implementation

## Overview

The Directed Graph (Digraph) Implementation is a Python program that provides a structure for representing directed graphs. This implementation allows users to create nodes and edges, calculate in-degrees and out-degrees of nodes, and perform basic graph operations. It is designed for educational purposes, demonstrating how graphs can be represented and manipulated in code.

## Features

- **Graph Representation**: Nodes and edges can be added to create a directed graph.
- **Degree Calculation**: Calculate in-degree and out-degree for any node in the graph.
- **Node Management**: Check for the existence of nodes within the graph.
- **String Representation**: Provides a readable format for visualizing the graph structure.

## Requirements

- Python 3.x
- `node.py` and `edge.py` files containing the `Node` and `Edge` classes, respectively.

## How to Use

1. Clone or download this repository.
2. Ensure the `node.py` and `edge.py` files are available in the same directory as this script.
3. Import the `Digraph` class into your Python script.

## Functions

### `add_node(node)`

Adds a node to the graph.

- **Inputs**: `node` - An instance of the `Node` class.
- **Outputs**: Raises a `ValueError` if the node already exists.

### `add_edge(edge)`

Adds a directed edge between two nodes.

- **Inputs**: `edge` - An instance of the `Edge` class.
- **Outputs**: Raises a `ValueError` if either node of the edge does not exist in the graph.

### `InDegree(node)`

Calculates and returns the in-degree of a specified node.

- **Inputs**: `node` - An instance of the `Node` class.
- **Outputs**: A string describing the in-degree of the node.

### `OutDegree(node)`

Calculates and returns the out-degree of a specified node.

- **Inputs**: `node` - An instance of the `Node` class.
- **Outputs**: A string describing the out-degree of the node.

### `has_node(node)`

Checks if a specific node exists in the graph.

- **Inputs**: `node` - An instance of the `Node` class.
- **Outputs**: `True` if the node exists, otherwise `False`.

### `__str__()`

Returns a string representation of the graph, showing the connections between nodes.

### `children_of(node)`

Returns a list of child nodes for a specified parent node.

- **Inputs**: `node` - An instance of the `Node` class.
- **Outputs**: A list of child nodes.

## Example Usage

To demonstrate the directed graph functionality, create instances of `Node` and `Edge`, add nodes to the `Digraph`, and create edges between the nodes. Calculate and print the in-degrees and out-degrees of specific nodes.

## Future Improvements

- **Graph Traversal Algorithms**: Implement additional graph algorithms such as Depth-First Search (DFS) and Dijkstra's algorithm.
- **Visualization**: Add graphical representation for easier understanding of graph structures.
- **User Interaction**: Create a user interface for dynamic graph creation and manipulation.

## License

This project is open-source and available.

---

**Author**: Alexander Harshman
