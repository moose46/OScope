from abc import ABC


class MyABC(ABC):
    hope = None


MyABC.register(tuple)

assert issubclass(tuple, MyABC)


@MyABC
class Hello:
    pass
