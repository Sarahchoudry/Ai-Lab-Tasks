#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Graph:
    def __init__(self):
        self.nodes = {
            "A": [("B", 6), ("F", 3)],
            "B": [("C", 3), ("D", 2)],
            "C": [("D", 1), ("E", 5)],
            "D": [("C", 1), ("E", 8)],
            "E": [("I", 5), ("J", 5)],
            "F": [("G", 1), ("H", 7)],
            "G": [("I", 3)],
            "H": [("I", 2)],
            "I": [("E", 5), ("J", 3)],
        }
        self.heuristics = {
            "A": 10,
            "B": 8,
            "C": 5,
            "D": 7,
            "E": 3,
            "F": 6,
            "G": 5,
            "H": 3,
            "I": 1,
            "J": 0,
        }
    def get_neighbors(self, node):
        return self.nodes.get(node, [])

    def calculate_heuristic(self, node):
        return self.heuristics.get(node, float('inf'))

    def find_shortest_path(self, start, goal):
        open_nodes = {start} 
        closed_nodes = set()  
        g_scores = {start: 0} 
        parents = {start: start}  
        
        while open_nodes:
            current_node = min(open_nodes, key=lambda node: g_scores[node] + self.calculate_heuristic(node))
            
            if current_node == goal:
                return self.reconstruct_path(parents, start, goal)
            
            open_nodes.remove(current_node)
            closed_nodes.add(current_node)
            
            for neighbor, weight in self.get_neighbors(current_node):
                if neighbor in closed_nodes:
                    continue
                
                tentative_g_score = g_scores[current_node] + weight
                
                if neighbor not in open_nodes:
                    open_nodes.add(neighbor)
                elif tentative_g_score >= g_scores.get(neighbor, float('inf')):
                    continue
                
                g_scores[neighbor] = tentative_g_score
                parents[neighbor] = current_node
        
        print("Path does not exist!")
        return None

    def reconstruct_path(self, parents, start, goal):
        path = []
        current_node = goal
        
        while current_node != start:
            path.append(current_node)
            current_node = parents[current_node]
        
        path.append(start)
        path.reverse()
        
        print(f"Path found: {path}")
        return path
graph = Graph()
graph.find_shortest_path("A", "J")


# In[ ]:





# In[ ]:





# In[ ]:




