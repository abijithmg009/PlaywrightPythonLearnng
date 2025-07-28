from FirstDemo import values

str = "RahulShettyAcademy.com"
print(str[1])
print(str[0:5]) # get substring from a large string


str1 = "consulting firm"


print(str+str1) #concatination

str3 = "RahulShetty"

print(str3 in str)

var = str.split(".")
print(var)
print(var[0])

#trim to remove white spaces

str4 = "   great     "
print(str4.strip())

#only left side
print(str4.lstrip())
print(str4.rstrip())