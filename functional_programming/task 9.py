def compose_functions(functions):
    def composed_function(arg):
        result = arg
        for func in functions:
            result = arg = func(arg)
        return result

    return composed_functions

