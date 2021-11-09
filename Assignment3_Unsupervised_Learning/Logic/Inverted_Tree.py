class Inverted_Tree:

    class Node:
        parent_1:Node
        parent_2:Node
        content:[int,int]

        def __init__(self):

        def set_parent_1(self,parent:Node):
            self.parent_1 = parent

        def set_parent_2(self,parent:Node):
            self.parent_2 = parent
