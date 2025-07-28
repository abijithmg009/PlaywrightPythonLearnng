print("Hello world")

#comments which needs to be defined.

a = 3
print(a)
print(type(a))

Str = "Hello world"
print(Str)

b,c,d = 4,5.6,"hello"

print(c)
print(d)

print(f"value is {a}")


values = [1,2,383,"thing"]
print(type(values))
print(values[3])
print(values[-1])
print(values[1:3])
values.append("end")
print(values[-1])
values.insert(3,"MG")

values[2] = "Abhi"
print(values[2])
del values[0]
print(values)

#Tiple
#list and tuple is same, but tuple is immutable but list is mutable. can be changed

a = (1,23,342,"ABhi","MG")
print(type(a))
#a[2] = "list"

#Dictionory - it has key value pair.

dict = {1:"Abhi",2:"MG","Log":34}
print(dict)
