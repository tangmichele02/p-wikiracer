from greedy import Greedy
from helper import PageRequestError
from algorithms.wikiracer import MaxPathLengthExceeded
from pytest import raises


#  1) where the destination page does not exists - works
# 2) where start page does not exist - running into a bug that 
# 3) not sure
def test_random_racer():
    gr = Greedy()
    gr.set_max_path_length(10)

    assert gr.max_path_length == 10

    # astronomically small probability this doesn't fail - Path is bigger than max path
    raises(MaxPathLengthExceeded, lambda: gr.find_path("Wikiracing", "Pomona College"))

    # Max path length must be at least 1
    raises(ValueError, lambda: gr.set_max_path_length(0))

    # Start Page does not exist 
    raises(PageRequestError, lambda: gr.find_path("Tilo RC", "Pomona College"))

    # Destination Page does not exist
    raises(PageRequestError, lambda: gr.find_path("Pomona College", "Tilo RC"))

    # an example that works is KIPP texas public schools and colorado river?
