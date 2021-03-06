from numpy import empty


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action



class Stack:
    def __init__(self):
        self.frontier = []
    
    def add(self, item: Node):
        self.frontier.append(item)
    
    def empty(self):
        return len(self.frontier) == 0

    def containsState(self, state):
        return any(node.state == state for node in self.frontier)

    def remove(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]

            return node

class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception('Empty Frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node