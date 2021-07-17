from functools import wraps
import functools
import time


def do_twice(func):
    @wraps(func)
    def wrapepr_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapepr_do_twice

    # We used *args and **kwargs so that it acan accept an arbitrary number of
    # positional and keyword arguments.


def timer(func):
    """Print the runtime of the decorated function"""

    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def debug(func):
    """Print the function signature and return value"""

    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat


# Defining decorator_repeat() as an inner function means that repeat() will refer
# to a function object—decorator_repeat. Earlier, we used repeat without
# parentheses to refer to the function object. The added parentheses are
# necessary when defining decorators that take arguments.

# The num_times argument is seemingly not used in repeat() itself. But by passing
# num_times a closure is created where the value of num_times is stored until it
# will be used later by wrapper_repeat().


def count_calls(func):
    @wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


# For a class instance to be callable, you implement the special .__call__()
# method:

# The .__call__() method is executed each time you try to call an instance of the
# class:

