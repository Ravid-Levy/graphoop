from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import os
def check0():
    h = DiGraph()  # creates an empty directed graph
    for n in range(4):
        h.add_node(n)
    h.add_edge(0, 1, 1)
    h.add_edge(1, 0, 1.1)
    h.add_edge(1, 2, 1.3)
    h.add_edge(2, 3, 1.1)
    h.add_edge(1, 3, 1.9)
    h.remove_edge(1, 3)
    h.add_edge(1, 3, 10)
    print(h)  # prints the __repr__ (func output)
    print(h.get_all_v())  # prints a dict with all the graph's vertices.
    print(h.all_in_edges_of_node(1))
    print(h.all_out_edges_of_node(1))
    g_algo = GraphAlgo(h)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = os.path.dirname(os.path.realpath(__file__))+"/data/A0"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    Galgor = GraphAlgo()
    file = os.path.dirname(os.path.realpath(__file__))+"/data/A5"
    Galgor.load_from_json(file)
    Galgor.get_graph().remove_edge(13, 14)
    Galgor.save_to_json(file + "_edited")
    dist, path = Galgor.shortest_path(1, 7)
    print(dist, path)
    dist, path = Galgor.shortest_path(47, 19)
    print(dist, path)
    dist, path = Galgor.shortest_path(20, 2)
    print(dist, path)
    dist, path = Galgor.shortest_path(2, 20)
    print(dist, path)
    print(Galgor.connected_component(0))
    print(Galgor.connected_components())
    Galgor.plot_graph()


if __name__ == '__main__':
    check0()
    check1()
    check2()
