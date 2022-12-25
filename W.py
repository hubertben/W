from commands import *
from stack import *

class Constraint:

    def __init__(self, init = []):
        self.stack = Stack(init = init)

    def printStacks(self, satisfier = []):
        print("------------------------")
        print("> Constraint")
        self.stack.display()
        if(len(satisfier.stack.stack) != 0):
            print("\n> Satisfier")
            satisfier.stack.display()
        print("------------------------")

    def executeScript(self, satisfier, verbose = False):
        i = 0

        while(True):

            if(verbose):
                print("")

            if(verbose):
                self.printStacks(satisfier)

            i += 1
            item = self.stack.popItem()

            if(len(self.stack) == -1):
                raise Exception("Bad")
            
            if(verbose):
                print(str(i), "\t", str(item), "\t", len(self.stack))

            args = []
            if(item in COMMANDS):

                if(verbose):
                    print("Item:", item)

                tempStack = Stack()
                satisfier.stack.moveTop(tempStack, COMMANDS[item][1])
                
                if(verbose):
                    self.printStacks(satisfier)
                    print("ARGS:", args)
                    print("TEMP STACK:", tempStack.stack)

                args = Stack()
                argsTemp = Stack()
                
                tempStack.moveAll(argsTemp)
                argsTemp.moveAll(args)

                args = args.stack

                print("ARGS:", args)

                if(len(args) != COMMANDS[item][1]):
                    raise Exception("Constraint Script contains extra command")
            

                object_ = item
                o = object_.execute(self = object_, a = args)
                if(verbose):
                    print("Executing:", str(object_), "on ARGS:", str(args), "->", o)
                self.stack.addItem(o)
                  
            else:

                if(len(self.stack) == 0):
                    self.stack.addItem(item)
                    break

                print("Non Command Item:", item)
                satisfier.stack.addItem(item)
            
            

        print("Stack:", self.stack.stack)
        print("Satisfier:", satisfier.stack.stack)
        return self.stack



class Satisfier:

    def __init__(self, init = []):
        self.stack = Stack(init = init)
        

            

# Basic Outline
# c = Constraint([])
# s = Satisfier([])
# c.executeScript(satisfier = s, verbose = True)


# Numeric Example
# c = Constraint([ADD, SUB, DIV])
# s = Satisfier([400, 20, 30, 4])
# c.executeScript(satisfier = s, verbose = True)


# Logic Example
# c = Constraint([False, NOT, AND, OR])
# s = Satisfier([True, False])
# c.executeScript(satisfier = s, verbose = True)

# Hashing Example
# i = 1
# h = HASHP().execute(i)
# c = Constraint([i, HASHP, EQUAL])
# s = Satisfier([h])
# c.executeScript(satisfier = s, verbose = True)


