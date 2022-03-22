class MyList(object):
    def __init__(self, data: list) -> None:
        self.data = data

    def __add__(self, other): return self.data + other.data

    def __mul__(self, other: int): return self.data * other
    def __rmul__(self, other: int): return  other * self.data

    def __str__(self) -> str: return str(self.data)
