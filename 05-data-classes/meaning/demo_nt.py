import typing

class DemoNTClass(typing.NamedTuple):
    a: int           # <1>
    b: float = 1.1   # <2>
    c = 'spam'       # <3>
nt = DemoNTClass(78)
print(nt.a)
print(nt.b)
print(nt.c)
