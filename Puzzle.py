# -*- coding: utf-8 -*-
"""
Created on 

"""
from Node import Node
from Problem import Problem


class Puzzle(Problem):

    def __init__(self, initial_state=(0, 0), final_state=(2, 0)):
        super().__init__(initial_state, final_state)

    def child_node(self, node):
        child = []

        i, j = self.manageMovs(node)
        son = self.movUP(node, i, j)
        if(son != None):
            child.append(son)

        i, j = self.manageMovs(node)
        son = self.movDOWN(node, i, j)
        if(son != None):
            child.append(son)

        i, j = self.manageMovs(node)
        son = self.movLEFT(node, i, j)
        if(son != None):
            child.append(son)

        i, j = self.manageMovs(node)
        son = self.movRIGHT(node, i, j)
        if(son != None):
            child.append(son)
        return child

    def movUP(self, node, i, j):
        if i > 0:
            # temp = []
            StateC = node.State
            temp = StateC[i][j]
            StateC[i][j] = StateC[i-1][j]
            StateC[i-1][j] = temp
            new_node = Node(StateC, parent=node, action='movUP')
            print(new_node.action, new_node.State)
            return new_node
        else:
            return None

    def movDOWN(self, node, i, j):
        if i > -1 and i < 2:
            # temp = []
            StateC = node.State
            temp = StateC[i+1][j]
            StateC[i+1][j] = StateC[i][j]
            StateC[i][j] = temp
            new_node = Node(StateC, parent=node, action='movDOWN')
            print(new_node.action, new_node.State)

            return new_node
        else:
            return None

    def movLEFT(self, node, i, j):
        if j > 0:
            # temp = []
            StateC = node.State
            temp = StateC[i][j-1]
            StateC[i][j-1] = StateC[i][j]
            StateC[i][j] = temp
            new_node = Node(StateC, parent=node, action='movLEFT')
            print(new_node.action, new_node.State)

            return new_node
        else:
            return None

    def movRIGHT(self, node, i, j):
        if j > -1 and j < 2:
            # temp = []
            StateC = node.State
            temp = StateC[i][j+1]
            StateC[i][j+1] = StateC[i][j]
            StateC[i][j] = temp
            new_node = Node(StateC, parent=node, action='movRIGHT')
            print(new_node.action, new_node.State)

            return new_node
        else:
            return None

    def locationZero(self, node):
        for elemento in node.State:
            if isinstance(elemento, list):
                # print (elemento)
                if 0 in elemento:
                    return node.State.index(elemento), elemento.index(0)

    def manageMovs(self, node):
        i, j = self.locationZero(node)
        return i, j
