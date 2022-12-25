
class ADD:
    def __init__(self): pass
    def execute(self, a, b = 0): return a + b if type(a) == int else a[0] + a[1]
    def __str__(self): return "ADD"

class SUB:
    def __init__(self): pass
    def execute(self, a, b = 0): return a - b if type(a) == int else a[0] - a[1]
    def __str__(self): return "SUB"

class MUL:
    def __init__(self): pass
    def execute(self, a, b = 0): return a * b if type(a) == int else a[0] * a[1]
    def __str__(self): return "MUL"

class DIV:
    def __init__(self): pass
    def execute(self, a, b = 0): return a / b if type(a) == int else a[0] / a[1]
    def __str__(self): return "DIV"

class AND:
    def __init__(self): self.and_ = False
    def execute(self, a, b = False): return (a and b) if type(a) != list else a[0] and a[1]
    def __str__(self): return "AND"

class OR:
    def __init__(self): self.or_ = False
    def execute(self, a, b = False): return (a or b) if type(a) != list else a[0] or a[1]
    def __str__(self): return "OR"

class NOT:
    def __init__(self): self.not_ = False
    def execute(self, a): return (not a) if type(a) != list else (not a[0])
    def __str__(self): return "NOT"

class ISZERO:
    def __init__(self): self.isZero = False
    def execute(self, a): return (a == 0) if type(a) != list else (a[0] == 0)
    def __str__(self): return "ISZERO"

class EQUAL:
    def __init__(self): self.equal = False
    def execute(self, a, b = False): return (a == b) if type(a) != list else (a[0] == a[1])
    def __str__(self): return "EQUAL"

COMMANDS = {
    ADD: ["ADD", 2], 
    SUB: ["SUB", 2], 
    MUL: ["MUL", 2], 
    DIV: ["DIV", 2],

    AND: ["AND", 2],
    OR: ["OR", 2],
    NOT: ["NOT", 1],
    ISZERO: ["ISZERO", 1],
    EQUAL: ["EQUAL", 2],
}


class Constraint:

    def __init__(self, init = []):
        self.stack = Stack(init = init)

    def run(self, satisfier, verbose = False):
        i = 0

        while(True):

            if(verbose):
                print("------------------------")
                print("> Constraint")
                self.stack.display()
                print("\n> Satisfier")
                satisfier.stack.display()
                print("------------------------")

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
                    print("------------------------")
                    print("> Constraint")
                    self.stack.display()
                    print("\n> Satisfier")
                    satisfier.stack.display()
                    print("------------------------")
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
            print("\t" + str(i))
        print(" --- Bottom of Stack ---")
        return ""

    def __len__(self):
        return len(self.stack)
            


# Adding numbers in the constraint script runs the commands in the order [constraint number, satisfier number (top of stack)]
# Adding numbers in the satisfier script runs the commands in the order [satisfier number (top of stack), satisfier number (2nd top of stack)]

# Basic Outline
# c = Constraint([])
# s = Satisfier([])
# c.run(satisfier = s, verbose = True)


# Numeric Example
# c = Constraint([ADD, SUB, DIV])
# s = Satisfier([400, 20, 30, 4])
# c.run(satisfier = s, verbose = True)


# Logic Example
# c = Constraint([False, NOT, AND, OR])
# s = Satisfier([True, False])
# c.run(satisfier = s, verbose = True)


c = Constraint([10, 7, SUB, EQUAL])
s = Satisfier([3])
c.run(satisfier = s, verbose = True)
