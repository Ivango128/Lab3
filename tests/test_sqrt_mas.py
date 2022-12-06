from lib import sqrt_mas

def test_sqrt_mas():
    assert sqrt_mas([1,2,3,-4,4]) == [1,1,1,2,2]