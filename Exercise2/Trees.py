#!/usr/bin/env python3
class Trees:
    pass


trees = Trees()


class Conifers(Trees):
    pass


class Deciduous(Trees):
    pass


conifers = Conifers()
deciduous = Deciduous()


class Pine(Conifers):
    pass


pine = Pine()


class Oak(Deciduous):
    pass


oak = Oak()

print(trees)
print(isinstance(trees, Trees))
print(isinstance(trees, object))

print(conifers)
print(isinstance(conifers, Conifers))
print(isinstance(conifers, Trees))
print(isinstance(conifers, object))

print(deciduous)
print(isinstance(deciduous, Deciduous))
print(isinstance(deciduous, Trees))
print(isinstance(deciduous, object))
print(isinstance(deciduous, Conifers))
print(isinstance(conifers, Deciduous))

print(oak)
print(isinstance(oak, Oak))
print(isinstance(oak, Deciduous))
print(isinstance(oak, Trees))
print(isinstance(oak, Conifers))
print(isinstance(oak, Pine))
print(isinstance(oak, object))

print(pine)
print(isinstance(pine, Pine))
print(isinstance(pine, Conifers))
print(isinstance(pine, Trees))
print(isinstance(pine, Deciduous))
print(isinstance(pine, Oak))
print(isinstance(pine, object))

