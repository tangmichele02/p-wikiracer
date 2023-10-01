from algorithms.random_racer import RandomRacer
from algorithms.wikiracer import MaxPathLengthExceeded
from pytest import raises
def test_random_racer():
    rr = RandomRacer(10)
    # astronomically small probability this doesn't fail
    raises(MaxPathLengthExceeded, lambda: rr.find_path("Wikiracing", "Pomona College"))

    # Max path length must be at least 1
    raises(ValueError, lambda: RandomRacer(0))
