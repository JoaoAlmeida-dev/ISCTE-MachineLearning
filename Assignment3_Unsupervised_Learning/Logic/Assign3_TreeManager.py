from binarytree import Node


class TreeManager:
    Assign3_Nodes_List: [Node]

    def __init__(self):
        self.Assign3_Nodes_List = []

    def get(self, content: [float, float]):
        for node in self.Assign3_Nodes_List:
            if node.val == content:
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
        print(self.Assign3_Nodes_List[-1])


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
