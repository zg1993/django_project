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


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print cls, name
        new_class = super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        # print hasattr(new_class, 'f')
        print dir(new_class)
        # new_class.f()
        # print attrs
        return new_class

    def f(cls):
        print cls


class Model:
    __metaclass__ = ModelMetaclass


class U(Model):
    pass