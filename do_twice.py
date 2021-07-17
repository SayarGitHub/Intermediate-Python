def do_twice(func):
    def wrapepr_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapepr_do_twice

    # We used *args and **kwargs so that it acan accept an arbitrary number of
    # positional and keyword arguments.
