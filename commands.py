


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

p = 560297606737113200709328709
q = 2147483647

class HASH:
    def __init__(self): self.hash = False
    def execute(self, a): return (a * p) % q if type(a) != list else (a[0] * p) % q
    def __str__(self): return "HASH"

class HASHP:
    def __init__(self): self.hashp = False
    def execute(self, a): return hash(str(a)) if type(a) != list else hash(str(a[0]))
    def __str__(self): return "HASHP"


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
    HASH: ["HASH", 1],
    HASHP: ["HASHP", 1]
}