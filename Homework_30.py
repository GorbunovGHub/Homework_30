def create_operation(operation):
    if operation == "division":
        def division(x, y):
            return x / y

        return division

    elif operation == "multiply":
        def multiply(x, y):
            return x * y

        return multiply


my_func_multiply = create_operation("multiply")
print(my_func_multiply(3, 2))
my_func_div = create_operation("division")
print(my_func_div(4, 2))
# my_func_div = create_operation("division")
# print(my_func_div(4, 0))


add = lambda x, y: x + y
print(add(8, 8))


def squaring_def(x, y):
    return x ** y


print(squaring_def(4, 2))


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'Стороны: {self.a}, {self.b}')

    def __call__(self):
        return f'Площадь: {self.a * self.b}'


my_rect = Rect(2, 4)
print(my_rect.__call__())
