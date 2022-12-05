
import math

class Wobject:

    def __init__(self, type_, value_):
        self.type_ = type_
        self.value_ = value_

class WobjectNumber(Wobject):

    def __init__(self, value_):
        super().__init__("number", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __add__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ + other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ + other)

    def __sub__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ - other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ - other)
        

    def __mul__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ * other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ * other)

    def __truediv__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ / other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ / other)

    def __pow__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ ** other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ ** other)

    def __mod__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectNumber(self.value_ % other.value_)
        elif isinstance(other, int) or isinstance(other, float):
            return WobjectNumber(self.value_ % other)

    def __lt__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ < other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ < other

    def __le__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ <= other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ <= other

    def __eq__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ == other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ == other

    def __ne__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ != other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ != other

    def __gt__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ > other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ > other

    def __ge__(self, other):
        if isinstance(other, WobjectNumber):
            return self.value_ >= other.value_
        elif isinstance(other, int) or isinstance(other, float):
            return self.value_ >= other

    def __abs__(self):
        return WobjectNumber(abs(self.value_))

    def __neg__(self):
        return WobjectNumber(-self.value_)

    def __pos__(self):
        return WobjectNumber(+self.value_)

    def __round__(self, n=None):
        return WobjectNumber(round(self.value_, n))

    def __floor__(self):
        return WobjectNumber(math.floor(self.value_))

    def __ceil__(self):
        return WobjectNumber(math.ceil(self.value_))

    def __trunc__(self):
        return WobjectNumber(math.trunc(self.value_))

    def __int__(self):
        return int(self.value_)

    def __float__(self):
        return float(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(str(self.value_))











class WobjectString(Wobject):

    def __init__(self, value_):
        super().__init__("string", value_)

    def __str__(self):
        return self.value_

    def __repr__(self):
        return self.value_

    def __add__(self, other):
        if isinstance(other, WobjectString):
            return WobjectString(self.value_ + other.value_)
        elif isinstance(other, WobjectNumber):
            return WobjectString(self.value_ + str(other.value_))

    def __mul__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectString(self.value_ * other.value_)

    def __lt__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ < other.value_

    def __le__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ <= other.value_

    def __eq__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ == other.value_

    def __ne__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ != other.value_

    def __gt__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ > other.value_

    def __ge__(self, other):
        if isinstance(other, WobjectString):
            return self.value_ >= other.value_

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(self.value_)

    def __getitem__(self, key):
        return WobjectString(self.value_[key])

    def __iter__(self):
        return iter(self.value_)

    def __contains__(self, item):
        return item in self.value_

    def __reversed__(self):
        return reversed(self.value_)

    def __int__(self):
        return int(self.value_)

    def __float__(self):
        return float(self.value_)

    def __round__(self, n=None):
        return round(self.value_, n)




class WobjectBoolean(Wobject):

    def __init__(self, value_):
        super().__init__("boolean", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __int__(self):
        return int(self.value_)

    def __float__(self):
        return float(self.value_)

    def __len__(self):
        return len(str(self.value_))



class WobjectList(Wobject):

    def __init__(self, value_):
        super().__init__("list", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __add__(self, other):
        if isinstance(other, WobjectList):
            return WobjectList(self.value_ + other.value_)

    def __mul__(self, other):
        if isinstance(other, WobjectNumber):
            return WobjectList(self.value_ * other.value_)

    def __lt__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ < other.value_

    def __le__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ <= other.value_

    def __eq__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ == other.value_

    def __ne__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ != other.value_

    def __gt__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ > other.value_

    def __ge__(self, other):
        if isinstance(other, WobjectList):
            return self.value_ >= other.value_

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(self.value_)

    def __getitem__(self, key):
        return self.value_[key]

    def __setitem__(self, key, value):
        self.value_[key] = value

    def __iter__(self):
        return iter(self.value_)

    def __contains__(self, item):
        return item in self.value_

    def __reversed__(self):
        return reversed(self.value_)

    def __int__(self):
        return int(self.value_)

    def __float__(self):
        return float(self.value_)

    def __round__(self, n=None):
        return round(self.value_, n)

    def append(self, item):
        self.value_.append(item)

    def extend(self, item):
        self.value_.extend(item)

    def insert(self, index, item):
        self.value_.insert(index, item)

    def remove(self, item):
        self.value_.remove(item)

    def pop(self, index=None):
        self.value_.pop(index)

    def index(self, item, start=None, stop=None):
        self.value_.index(item, start, stop)



class WobjectNull(Wobject):

    def __init__(self, value_):
        super().__init__("null", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(str(self.value_))

    

class WobjectUndefined(Wobject):

    def __init__(self, value_):
        super().__init__("undefined", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(str(self.value_))




class WobjectOperator(Wobject):

    def __init__(self, value_):
        super().__init__("operator", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(str(self.value_))




class WobjectVariable(Wobject):

    def __init__(self, value_):
        super().__init__("variable", value_)

    def __str__(self):
        return str(self.value_)

    def __repr__(self):
        return str(self.value_)

    def __bool__(self):
        return bool(self.value_)

    def __hash__(self):
        return hash(self.value_)

    def __len__(self):
        return len(str(self.value_))