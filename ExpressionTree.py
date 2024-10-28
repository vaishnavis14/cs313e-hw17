
#  File: ExpressionTree.py

#  Description: Given a tree filled with expressions, evaluate and sort in different notations

#  Student Name: Saivachan Ponnapalli

#  Student UT EID: sp48347

#  Partner Name: Vaishnavi Sathiyamoorthy

#  Partner UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/04/2022

#  Date Last Modified: 11/07/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = lChild

class Tree (object):
    def __init__ (self):
        self.root = None
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        current =self.root =Node()  # had to initialize self.root to a Node
        stack= Stack()
        new= expr.split(" ")
        for i in new:  # goes through the for loop to evaluate the different parts of the tree and create the tree
            if i== "(":
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            elif i == ")":
                if not stack.is_empty():
                    current = stack.pop()
            elif i in operators:
                current.data = i
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            else:
                current.data = i
                current = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):  # evaluate function using operate taught in class
        if (aNode.data in operators):
            return self.operate(self.evaluate(aNode.lChild), self.evaluate(aNode.rChild), aNode.data)
        else:

            return float(aNode.data)  # recursive method

    def operate(self, oper1, oper2, token):  # operate function given in class with RPN
        expr = str(oper1) + token + str(oper2)
        return eval(expr)

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):  # pre order function to print it out through a stack
        stack = Stack()
        stack.push(aNode)

        returner = ""
        while (curr := stack.pop()):
            returner += curr.data + " "

            if curr.rChild: stack.push(curr.rChild)
            if curr.lChild: stack.push(curr.lChild)

        return returner

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        # pre order expression that takes the nodes in a stack and prints it through the stack
        stack1 = Stack()
        stack2 = Stack()  # using 2 stacks to rearrange and bring the post order expression
        stack1.push(aNode)

        while not stack1.is_empty():
            curr = stack1.pop()
            stack2.push(curr)
            if (curr.lChild): stack1.push(curr.lChild)
            if (curr.rChild): stack1.push(curr.rChild)
        returner = ""
        while (curr := stack2.pop()):
            returner += curr.data + " "
        return returner


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()