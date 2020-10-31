#
# C H A P T E R  2
# ------------------------
# C A L L A B L E
#

if __name__ == '__main__':
    # 1. C L O S U R E: a place with functions and has data attached (different from class where is a place with data and has functions attached)
    # e.g
    class Adder:
        def __init__(self, n):
            self.n = n

        def __call__(self, m):
            return self.n + m

    # closure
    def make_adder(n):
        def adder(m):
            return m + n
        return adder

    adder_i = Adder(5)
    adder_f = make_adder(5)
    assert adder_i.n == 5, "Expected 5"
    assert adder_i(5) == 10, "Expected 10"
    assert adder_f(5) == 10, "Expected 10"
    adder_i.n = 10  # State is readily and changeable (this against FP "Immutable" principle)
    assert adder_i.n == 10, "Expected 10"
    assert adder_i(10) == 20, "Expected 20"

    adders = []
    for n in range(5):
        adders.append(lambda m, n=n: m+n)
    print([adder(10) for adder in adders])

    adder_4 = adders[4]
    print(adder_4(1, 100))


    # Class with @staticmethod: Using classes simply as namespaces to hold a variety of related functions
    class RightTriangle:

        @staticmethod
        def hypotenuse(a, b):
            import math
            return math.sqrt(a**2 + b**2)


        @staticmethod
        def sin(a, b):
            return a / RightTriangle.hypotenuse(a, b)

    # e.g
    print("hypotenuse:>", RightTriangle.hypotenuse(3, 4))
    print("sin:>", RightTriangle.sin(3, 4))

    # Generator
    def get_primes():
        candidate = 2
        found = []
        while True:
            if all(candidate % prime != 0 for prime in found):
                yield candidate
                found.append(candidate)
            candidate += 1

    primes = get_primes()
    print(next(primes), next(primes), next(primes), next(primes))
    print(next(primes))

    # Multiple Dispatch: Avoiding or reducing use of condition branching
    # by declaring multiple signatures for a single function and call the actual computation
    # that matches the types or properties of the calling arguments

    # e.g Rock, Paper, Scissors
    class Thing:
        pass

    class Rock(Thing):
        pass

    class Paper(Thing):
        pass

    class Scissors(Thing):
        pass
    # conditional branching approach
    def beats_cb(x, y):
        if isinstance(x, Rock):
            if isinstance(y, Rock):
                return None  # No winner
            elif isinstance(y, Paper):
                return y
            elif isinstance(y, Scissors):
                return x
            else:
                raise TypeError("Unknown second thing")
        elif isinstance(x, Paper):
            if isinstance(y, Rock):
                return x
            elif isinstance(y, Paper):
                return None  # No winner
            elif isinstance(y, Scissors):
                return y
            else:
                raise TypeError("Unknown second thing")
        elif isinstance(x, Scissors):
            if isinstance(y, Rock):
                return y
            elif isinstance(y, Paper):
                return x
            elif isinstance(y, Scissors):
                return None  # No winner
            else:
                raise TypeError("Unknown second thing")
        else:
            raise TypeError("Unknown first thing")

    # duck-typing approach
    class DuckRock(Rock):
        def beats(self, other):
            if isinstance(other, Rock):
                return None  # No winner
            elif isinstance(other, Paper):
                return other
            elif isinstance(other, Scissors):
                return self
            else:
                raise TypeError("Unknown target")


    class DuckPaper(Paper):
        def beats(self, other):
            if isinstance(other, Rock):
                return self
            elif isinstance(other, Paper):
                return None  # No winner
            elif isinstance(other, Scissors):
                return other
            else:
                raise TypeError("Unknown target")


    class DuckScissors(Scissors):
        def beats(self, other):
            if isinstance(other, Rock):
                return other
            elif isinstance(other, Paper):
                return self
            elif isinstance(other, Scissors):
                return None  # No winner
            else:
                raise TypeError("Unknown target")


    # multiple dispatch approach
    # ? NOT standar in Python. https://github.com/mrocklin/multipledispatch