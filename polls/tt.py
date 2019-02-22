# encoding: utf8


def decorator(cls):
    print cls


# @decorator
class A:
    def f(self):
        print self
    name = 'zz'
    n = property(f)
    pass

print dir(A)
print A.n
