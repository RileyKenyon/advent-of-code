from os import name
import sys
from enum import Enum, unique

class NodeType(Enum):
    SMALL_NODE = 0
    LARGE_NODE = 1

class Node(object):
    def __init__(self,name) -> None:
        self.adjacent_nodes = set()
        self.name = name
        self.node_type = NodeType.LARGE_NODE if self.is_large_cave() else NodeType.SMALL_NODE
        self.num_visits = 0
    
    def __eq__(self, other_node):
        if isinstance(other_node, Node):
            return self.name == other_node.name
    
    def __hash__(self) -> int:
        return super().__hash__()

    def is_large_cave(self) -> bool:
        return self.name.isupper()

class Graph:
    def __init__(self) -> None:
        self.start_node: Node
        self.end_node: Node
        self.nodes = dict()
        # self.visited_path = set()
        self.num_paths = 0
        self.max_num_visits = 2

    def create_node(self,node_name: str):
        # print('Node: {0} already exists in graph'.format(node.name))
        self.nodes[node_name] = Node(node_name)
        if node_name == 'start':
            self.start_node = self.nodes[node_name]
        elif node_name == 'end':
            self.end_node = self.nodes[node_name]

    def link_nodes(self,node_a, node_b):
        self.nodes[node_a].adjacent_nodes.add(self.nodes[node_b])
        self.nodes[node_b].adjacent_nodes.add(self.nodes[node_a]) 

    def traverse_nodes(self, node, visited_path = set()):
        # Traverse nodes as long as not end node
        path_len = 0
        if node != self.end_node:
            for cave in node.adjacent_nodes:
                # Cannot go back to the start node
                if cave != self.start_node:
                    # Add cave to visited path if not there
                    # if cave.name not in visited_path:
                        # self.visited_path |= {cave.name}
                    # Don't allow small nodes to be visited more than max_visit
                    if not cave.is_large_cave():
                        if cave.num_visits < self.max_num_visits:
                            cave.num_visits+=1              
                            path_len+=self.traverse_nodes(cave, visited_path | {cave.name})
                        else:
                            continue
                    else:
                        cave.num_visits+=1              
                        path_len+=self.traverse_nodes(cave, visited_path)
        else:
            # clear visited path 
            # self.visited_path = set()
            # for node in self.nodes.values():
                # node.num_visits = 0
            path_len = 1
            
        return path_len

    def get_num_paths(self):
        # Call traverse_nodes from starting node
        return self.traverse_nodes(self.start_node)


# def traverse_nodes(node, visited_nodes = set()):
#     if node == "end":
#         return 1
#     num_paths = 0
#     for next_node in node_list[node]:
#         if next_node in visited_nodes: continue
#         num_paths+=traverse_nodes(next_node, visited_nodes | {node} if node == node.lower() else visited_nodes)
#     return num_paths

def main():
    """
    --- Day 12: Passage Pathing ---
    Find best path through cave

    start-A 
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end

        start
        /   \
    c--A-----b--d
        \   /
        end
    
    Find the number of distinct paths that start at start and end at end, don't visit small caves (lowercase) more than once
    Big caves (uppercase) can be visited multiple times
    """
    # global node_list
    fname = sys.argv[1]
    g = Graph()
    with open(fname,'r') as f:
        parsed_nodes = [line.split('-') for line in f.read().splitlines()]

        # Create unique nodes for each
        unique_names = set([j for i in parsed_nodes for j in i])
        for name in unique_names:
            g.create_node(name)

        # Add in linkage between nodes
        for n1, n2 in parsed_nodes:
            g.link_nodes(n1,n2)
        
        # # Get number of paths
        num_paths = g.get_num_paths()
        print(num_paths)
        #     print(n1,n2)
        #     node_list[n1] = node_list.get(n1,[]) + [n2]
        #     node_list[n2] = node_list.get(n2,[]) + [n1]
        # # print(count("start"))
        # num_paths = traverse_nodes("start")
        # print(num_paths)
            # if nodes == []:
            #     first_node = Node(n1)
            #     second_node = Node(n2)
            #     first_node.attach(second_node)
            #     second_node.attach(first_node)
            #     nodes.append(Node(n1),Node(n2))
            # # else:
            #     if 
            

if __name__ == "__main__":
    main()