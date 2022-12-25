
from commands import *

# Front of Stack [ _, _, _, ... _, _, _ ] Back of Stack
class Stack:

    def __init__(self, init = []):
        self.stack = [] if init == [] else init

    def addItem(self, item):
        self.stack.insert(0, item)

    def popItem(self):
        if(len(self.stack) == 0):
            return None
        return self.stack.pop(0)

    def peekTop(self):
        if(len(self.stack) == 0):
            return None
        return self.stack[0]

    def moveTop(self, otherStack, itter = 1):
        for _ in range(itter):
            item = self.popItem()
            if(item != None):
                otherStack.addItem(item)
        
    def moveAll(self, otherStack):
        l = len(self.stack)
        for _ in range(l):
            item = self.popItem()
            if(item != None):
                otherStack.addItem(item)

    def __str__(self):

        printStack = []

        for i in self.stack:
            if(i in COMMANDS):
                l = len(COMMANDS[i][0])
                printStack = str(i)[len(str(i)) - 5 : len(str(i)) - 2]

        return str(printStack)

    def display(self):
        print(" ----  Top of Stack  ---")
        for i in self.stack:
            if(i in COMMANDS):
                l = COMMANDS[i][0]
                print("  ", l)
            else:
                print("  ", i)
        print(" --- Bottom of Stack ---")
        return ""

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, key):
        return self.stack[key]

    def __setitem__(self, key, value):
        self.stack[key] = value

    def __delitem__(self, key):
        del self.stack[key]

    def __iter__(self):
        return iter(self.stack)

    def __reversed__(self):
        return reversed(self.stack)

    def __contains__(self, item):
        return item in self.stack