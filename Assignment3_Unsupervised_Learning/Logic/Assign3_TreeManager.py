from binarytree import Node

COUNT = 10


class Node:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    # Function to print binary tree in 2D
    # It does reverse inorder traversal
    @classmethod
    def print2DUtil(cls, root, space, maxdepth):
        currdepth = space / COUNT

        # Base case
        if root is None or currdepth > maxdepth:
            return

        # Increase distance between levels
        space += COUNT

        # Process right child first
        Node.print2DUtil(root.right, space, maxdepth)

        # Print current node after space
        for i in range(COUNT, space):
            print(end=" ")
        print(root.data)

        # Process left child
        Node.print2DUtil(root.left, space, maxdepth)

    # Wrapper over print2DUtil()
    @classmethod
    def print2D(cls, root, depth: int):
        # space=[0]
        # Pass initial space count as 0
        Node.print2DUtil(root, 0, depth)


class TreeManager:
    Assign3_Nodes_List: [Node]

    def __init__(self):
        self.Assign3_Nodes_List = []

    def get(self, content: [float, float]):
        for node in self.Assign3_Nodes_List:
            if node.data == content:
                return node
        return Node(content)

    def exists(self, node: Node) -> bool:
        return node in self.Assign3_Nodes_List

    def add(self, node: Node):
        if not self.exists(node):
            self.Assign3_Nodes_List.append(node)
        else:
            raise Exception(node, "Node already exists in Tree")

    def build(self):
        depth = 3
        print("----------FirstNode----------")
        print(Node.print2D(self.Assign3_Nodes_List[-1], depth))
        print("----------SecondNode----------")
        print(Node.print2D(self.Assign3_Nodes_List[-2], depth))

    @classmethod
    def get_all_parents(cls, root_node: Node):
        def aux(children_list: list, node: Node):
            children_list.append(node)
            if node.right is not None:
                aux(children_list=children_list, node=node.right)
            if node.left is not None:
                aux(children_list=children_list, node=node.left)

        children: [Node] = []
        aux(node=root_node, children_list=children)
        return children



if __name__ == '__main__':
    treeManager = TreeManager()
    node1: Node = Node(2.1310)
    parent1: Node = Node(1.232)
    parent2: Node = Node(-1.1231)

    node1.right = parent1
    node1.left = parent2

    treeManager.add(parent2)
    treeManager.add(parent1)
    treeManager.add(node1)

    treeManager.build()
