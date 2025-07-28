

class my_class:
    @classmethod
    def my_class(cls):
        return "class"

    def instance_method(self):
        return "instance"

obj = my_class()


print(obj.instance_method())

print(my_class.my_class())
print(my_class.my_class())