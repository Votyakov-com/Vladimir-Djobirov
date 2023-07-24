def compose(f, g):
    h = lambda arg: g(f(arg))
    return h
