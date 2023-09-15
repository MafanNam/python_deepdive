def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run")

        return result

    return inner


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


# print(calc_recursive_fib(100))

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)


# fib_recursive(40)

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(2, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2


# print(fib_loop(100))

from functools import reduce


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]


# print(fib_reduce(100))


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        return result
    return inner

@logged
def f():
    pass

# print(f())

@timed
@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

# print(fact(5))




# print(fib(10))

@timed
class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}


    def fib(self, n):
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self.fib(n-1) + self.fib(n-2)

        return self.cache[n]

# f = Fib()
#
# print(f.fib(10))

@timed
def memorize(fib):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)

        return cache[n]

    return inner


# @memorize
def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# print(fib(10))
# print(fib(11))
# print(fib(12))
# print(fib(13))
# print(fib(20))
# print(fib(40))
# print(fib(50))

# print(f(10))

# @timed
# @memorize
def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


# print(fact(100))



def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={a}, b={b}')
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def mu_func(s):
    print(f"Hello {s}")

# print(mu_func('Test'))


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={self.a}, b={self.b}')
            return fn(*args, **kwargs)

        return inner

@MyClass(99, 33)
def mu_func(s):
    print(f"Hello {s}")


# print(mu_func('dd'))















