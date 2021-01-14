from src.GraphInterface import GraphInterface
from random import randint


class DiGraph(GraphInterface):

    def __init__(self):
        self.Nodes = dict()
        self.Edges =dict()
        self.EdgesIn =dict()
        self.MC =0
        self.ESIZE =0

    def v_size(self):
        return len(self.Nodes)

    def e_size(self):
        return self.ESIZE

    def get_all_v(self):
        return self.Nodes

    def all_in_edges_of_node(self, id1: int):
        return self.EdgesIn[id1]

    def all_out_edges_of_node(self, id1: int):
        return self.Edges[id1]

    def get_mc(self):
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float):
        if weight<0:
            print("weight < 0")
            return False
        if id1 not in self.Nodes.keys() or id2 not in self.Nodes.keys():
            return False
        else:
            if id2 not in self.Edges[id1].keys():
                self.ESIZE+=1
            else:
                self.Edges[id1].pop(id2)
                self.EdgesIn[id2].pop(id1)
            self.Edges[id1].update({id2:weight})
            self.EdgesIn[id2].update({id1:weight})
            self.MC+=1
            return True

    def add_node(self, node_id: int, pos: tuple = None):
        if not (self.Nodes.__contains__(node_id)):
            if pos is not None:
               self.Nodes.update({node_id: {pos}})
            else:
                self.Nodes.update({node_id:
                    [randint(0,10000),
                    randint(0,10000)]
                                   })
            self.Edges.update({node_id: {}})
            self.EdgesIn.update({node_id: {}})
            self.MC = self.MC + 1
            return True
        return False

    def remove_node(self, node_id: int):
        if node_id in self.Nodes:
            for i in self.EdgesIn[node_id].keys():
                self.Edges[i].pop(node_id)
                self.ESIZE -= 1

            for i in self.Edges[node_id].keys():
                self.EdgesIn[i].pop(node_id)
                self.ESIZE -= 1

            self.EdgesIn.pop(node_id)
            self.Edges.pop(node_id)
            self.Nodes.pop(node_id)
            self.MC+=1
            return True

        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 not in self.EdgesIn[node_id2].keys() or node_id2 not in self.Edges[node_id1].keys():
            return False
        else:
            self.Edges[node_id1].pop(node_id2)
            self.EdgesIn[node_id2].pop(node_id1)
            self.MC += 1
            self.ESIZE += 1
            return True