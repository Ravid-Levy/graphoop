## graphoop

directed weighted graph implement same like ex2 Graph
The TASK compares between python and java graphs.

About the classes:
## DiGraph.py
init(self): Init this graph
<br />
v_size(): Returns the number of nodes in this graph.
<br />
e_size(): Returns the number of edges in this graph
<br />
all_in_edges_of_node - return a dictionary of all the nodes connected to into node_id, each node is Pair (key, weight).
<br />
all_out_edges_of_node - return a dictionary of all the nodes connected from node_id, each node is Pair (key, weight).
<br />
get_mc() - MC is count of the changes on graph.
<br />
add_edge() - Adds an edge to the graph.
<br />
remove_node() - Removes a node from the graph
<br />
remove_edge() - Removes an edge from the graph

## GraphAlgo.py
init () - init the graph.
<br />
get_graph() - return the graph 
<br />
load_from_json() - Loads a graph from a json file.
<br />
save_to_json - save a graph to a json file. 
<br />
Shortest_path() - Returns the shortest path between two nodes id1 to id2.
<br />
connected_component() - Finds the Strongly Connected Component that node id1 is a part of.
<br />
plot_graph() - Plots the graph.
