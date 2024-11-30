#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Vertex:
    def __init__(self, label):
        self.label = label
        self.connections = []

    def connect(self, vertex):
        self.connections.append(vertex)

def depth_first_search(start_vertex, explored=None):
    if explored is None:
        explored = set()  
    if start_vertex not in explored:
        print(start_vertex.label)
        explored.add(start_vertex)
        
        for adjacent in start_vertex.connections:
            if adjacent not in explored:
                depth_first_search(adjacent, explored)

vertex_1 = Vertex('X')
vertex_2 = Vertex('Y')
vertex_3 = Vertex('Z')
vertex_4 = Vertex('W')
vertex_5 = Vertex('V')

vertex_1.connect(vertex_2)
vertex_1.connect(vertex_3)
vertex_2.connect(vertex_4)
vertex_3.connect(vertex_5)
vertex_4.connect(vertex_1) 
vertex_5.connect(vertex_2)

depth_first_search(vertex_1)


# In[9]:


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def traverse_inorder(node):
    if node:
        traverse_inorder(node.left_child)
        print(node.data, end=' ')
        traverse_inorder(node.right_child)

def traverse_preorder(node):
    if node:
        print(node.data, end=' ')
        traverse_preorder(node.left_child)
        traverse_preorder(node.right_child)

def traverse_postorder(node):
    if node:
        traverse_postorder(node.left_child)
        traverse_postorder(node.right_child)
        print(node.data, end=' ')

root_node = TreeNode(10)
root_node.left_child = TreeNode(20)
root_node.right_child = TreeNode(30)
root_node.left_child.left_child = TreeNode(40)
root_node.left_child.right_child = TreeNode(50)

print("Inorder Traversal:")
traverse_inorder(root_node)
print("\nPreorder Traversal:")
traverse_preorder(root_node)
print("\nPostorder Traversal:")
traverse_postorder(root_node)



# In[ ]:





# In[ ]:




