class Example:
    class_var = "I am a class variable"

    def __init__(self, value):
        self.instance_var = value

    def show(self):
        local_var = "I am a local"
        print(local_var, self.instance_var, Example.class_var)

example = Example("Instance Variable")
example.show()

sum_number = 0
def a_function(number):
    sum_number = 1
    number = sum_number

a_function(2)
print(sum_number)