class UFNode():
    def __init__(self, node_str: str):
        self.node_str = node_str
        self.parent_node = None
    
    def set_parent(self, new_parent_node):  # new_parent_node should be type UFNode
        self.parent_node = new_parent_node

class UnionFind():
    def __init__(self):
        self.nodes = {} # {node_string:UFNode}
        self.component_sizes = {}  # {parent_str:component_size}
    
    def add_node_str(self, node_str: str):
        self.nodes[node_str] = UFNode(node_str)
        self.component_sizes[node_str] = 1

    def find(self, node_str: str):
        current_node = self.nodes[node_str]
        while current_node.parent_node:
            current_node = current_node.parent_node
        return current_node.node_str
    
    def union(self, n1_str: str, n2_str: str):  # merge smaller component into larger
        n1_leader, n2_leader = self.find(n1_str), self.find(n2_str)
        if self.component_sizes[n1_leader] > self.component_sizes[n2_leader]:
            larger, smaller = n1_leader, n2_leader
        else:
            smaller, larger = n1_leader, n2_leader
        # add the size of the smaller component to that of the larger
        self.component_sizes[larger] += self.component_sizes[smaller]
        # delete the smaller from component_sizes
        del self.component_sizes[smaller]
        # update all parent pointers in smaller to point to larger 
        self.nodes[smaller].parent_node = self.nodes[larger]