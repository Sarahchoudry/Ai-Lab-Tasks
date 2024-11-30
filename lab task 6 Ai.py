#!/usr/bin/env python
# coding: utf-8

# In[10]:


from collections import deque

def breadth_first_search(graph_structure, starting_node):
    explored_nodes = set() 
    node_queue = deque([starting_node])
    while node_queue:
        current_node = node_queue.popleft() 
        if current_node not in explored_nodes:
            print(current_node)
            explored_nodes.add(current_node) 
            for adjacent_node in graph_structure[current_node]:
                if adjacent_node not in explored_nodes:
                    node_queue.append(adjacent_node)
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

breadth_first_search(graph_data, 'A')



# In[11]:


from collections import deque

class GraphElement:
    def __init__(self, identifier):
        self.identifier = identifier
        self.adjacent_nodes = []
    def link(self, node):
        self.adjacent_nodes.append(node)

def breadth_first_traversal(start_element):
    visited_set = set() 
    element_queue = deque([start_element])  
    
    while element_queue:
        current_element = element_queue.popleft() 
        if current_element not in visited_set:
            print(current_element.identifier) 
            visited_set.add(current_element)  
            for neighbor in current_element.adjacent_nodes:
                if neighbor not in visited_set:
                    element_queue.append(neighbor)
node_1 = GraphElement('X')
node_2 = GraphElement('Y')
node_3 = GraphElement('Z')
node_4 = GraphElement('W')
node_5 = GraphElement('V')

node_1.link(node_2)
node_1.link(node_3)
node_2.link(node_4)
node_2.link(node_5)
node_3.link(node_5)

breadth_first_traversal(node_1)


# In[ ]:





# In[ ]:




