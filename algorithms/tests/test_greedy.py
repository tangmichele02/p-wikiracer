from greedy import Greedy
from algorithms.wikiracer import MaxPathLengthExceeded
from pytest import raises


#  1) where the destination page does not exists - works
# 2) where start page does not exist - running into a bug that 
# 3) where
def test_random_racer():
    gr = Greedy()
    gr.set_max_path_length(10)

    assert gr.max_path_length == 10

    # astronomically small probability this doesn't fail
    raises(MaxPathLengthExceeded, lambda: gr.find_path("Wikiracing", "Pomona College"))

    # start page does not exist
    raises(ValueError, lambda: gr.find_path("Tilo RC", "Pomona College"))

    # target page does not exist
    raises(ValueError, lambda: gr.find_path("Pomona College"))

    # exceeds max path
    raises(ValueError, lambda: gr.find_path("Pomona College", "Gavin Newsom"))

