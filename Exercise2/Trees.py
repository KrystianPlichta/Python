#!/usr/bin/env python3
class Tree:
    pass


tree = Tree()


class Conifers(Tree):
    pass


class Deciduous(Tree):
    pass


conifers = Conifers()
deciduous = Deciduous()


class Pine(Conifers):
    pass


pine = Pine()


class Oak(Deciduous):
    pass


oak = Oak()

print(tree)
print(isinstance(tree, Tree))
print(isinstance(tree, object))

print(conifers)
print(isinstance(conifers, Conifers))
print(isinstance(conifers, Tree))
print(isinstance(conifers, object))

print(deciduous)
print(isinstance(deciduous, Deciduous))
print(isinstance(deciduous, Tree))
print(isinstance(deciduous, object))
print(isinstance(deciduous, Conifers))
print(isinstance(conifers, Deciduous))

print(oak)
print(isinstance(oak, Oak))
print(isinstance(oak, Deciduous))
print(isinstance(oak, Tree))
print(isinstance(oak, Conifers))
print(isinstance(oak, Pine))
print(isinstance(oak, object))

print(pine)
print(isinstance(pine, Pine))
print(isinstance(pine, Conifers))
print(isinstance(pine, Tree))
print(isinstance(pine, Deciduous))
print(isinstance(pine, Oak))
print(isinstance(pine, object))

