from commands import *
from stack import *

class Constraint:

    def __init__(self, init = []):
        self.stack = Stack(init = init)

    def printStacks(self, satisfier = []):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("> Constraint")
        self.stack.display()
        if(satisfier != []):
            print("\n> Satisfier")
            satisfier.stack.display()
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

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
                
                if(verbose):
                    print("ARGS:", args)

                if(len(args) != COMMANDS[item][1]):
                    raise Exception("Constraint Script contains extra command")
            

                object_ = item
                o = object_.execute(self = object_, a = args)
                if(verbose):
                    print("\nExecuting:", str(COMMANDS[object_][0]), "on ARGS:", str(args), "->", o, "\n")
                self.stack.addItem(o)
                  
            else:

                if(len(self.stack) == 0):
                    self.stack.addItem(item)
                    break

                if(verbose):
                    print("Non Command Item:", item)
                satisfier.stack.addItem(item)
            
            
        if(verbose):
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

# Password is input by user
# password = 1234

# h is computed when the user creates the account
# h = HASHP().execute(password)

# Check if password is correct
# c = Constraint([password, HASHP, EQUAL])
# s = Satisfier([h])
# print(c.executeScript(satisfier = s, verbose = False).stack)



# POW Example

# s = 15
# e = s ** 3

# c = Constraint([3, POW, e, EQUAL])
# s = Satisfier([s])
# c.executeScript(satisfier = s, verbose = True)



# MOD Example: Checks if the hash of p is even/odd

# p = 27

# c = Constraint([p, HASH, 2, MOD, 1, EQUAL])
# s = Satisfier([])
# c.executeScript(satisfier = s, verbose = True)