def overload(arg):
    print(arg)

    def outer(function_to_decorate):
        def a_wrapper_accepting_arbitrary_arguments(*args):
            result = function_to_decorate(*args)
            return result

        return a_wrapper_accepting_arbitrary_arguments

    return outer


@overload('one')
def function(x):
    print("Один аргумент {}", x)


@overload('two')
def function(x, b):
    print('Два аргумента {},{}', x, b)


@overload('tree')
def function(a, b, c):
    print("Три аргумента")

    overload('one').function(1)
