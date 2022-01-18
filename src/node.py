import random

class Node:

    def __init__(self, value=None, weight=0, prob=0):
        self.value = value
        self.weight = weight
        self.prob = prob
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        self.calc_prob()

    def add_children(self, *nodes):
        for node in nodes:
            self.add_child(node)

    def calc_prob(self):
        weights = 0
        for child in self.children:
            weights += child.weight
        
        for child in self.children:
            child.prob = (child.weight / weights) * 100

    def get_child(self, idx):
        return self.children[idx]

    def choose_child(self, weighted=True):
        if not weighted: return self.children[0]
        
        rnd = random.randint(1, 100)

        c = 0
        for child in self.children:
            if rnd <= child.prob + c:
                return child.value
        
            c += child.prob