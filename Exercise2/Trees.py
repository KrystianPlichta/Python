#!/usr/bin/env python3
class Trees:
    pass


trees = Trees()


class Conifer(Trees):
    pass


class Deciduous(Trees):
    pass


conifer = Conifer()
deciduous = Deciduous()


class Pine(Conifer):
    pass


pine = Pine()


class Oak(Deciduous):
    pass


oak = Oak()

print(trees)
print(isinstance(trees, Trees))
print(isinstance(trees, object))

print(conifer)
print(isinstance(conifer, Conifer))
print(isinstance(conifer, Trees))
print(isinstance(conifer, object))

print(deciduous)
print(isinstance(deciduous, Deciduous))
print(isinstance(deciduous, Trees))
print(isinstance(deciduous, object))
print(isinstance(deciduous, Conifer))
print(isinstance(conifer, Deciduous))

print(oak)
print(isinstance(oak, Oak))
print(isinstance(oak, Deciduous))
print(isinstance(oak, Trees))
print(isinstance(oak, Pine))
print(isinstance(oak, object))

print(pine)
print(isinstance(pine, Pine))
print(isinstance(pine, Conifer))
print(isinstance(pine, Trees))
print(isinstance(pine, Oak))
print(isinstance(pine, object))
