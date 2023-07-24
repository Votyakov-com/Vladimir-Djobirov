def partical_apply(func, arg1, arg2):
    partical_func = lambda arg1: func(arg1)
    return partical_func
