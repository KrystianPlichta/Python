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


class Pines(Conifers):
    pass


pines = Pines()


class Oaks(Deciduous):
    pass


oaks = Oaks()

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

print(oaks)
print(isinstance(oaks, Oaks))
print(isinstance(oaks, Deciduous))
print(isinstance(oaks, Trees))
print(isinstance(oaks, Conifers))
print(isinstance(oaks, Pines))
print(isinstance(oaks, object))

print(pines)
print(isinstance(pines, Pines))
print(isinstance(pines, Conifers))
print(isinstance(pines, Trees))
print(isinstance(pines, Deciduous))
print(isinstance(pines, Oaks))
print(isinstance(pines, object))

