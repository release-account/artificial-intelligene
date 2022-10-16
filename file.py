from logic import *

rain = Symbol("rain") # it's raining
hagrid = Symbol("hagrid") # harry visted hagraid.
dumbledore = Symbol("dumbledore") # harry visted dumbledore.
sentence = And(rain,hagrid)

knowledge = Not(rain)
print(sentence.formula())