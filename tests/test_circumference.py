import pytest
from circumference import circumference



@pytest.mark.parametrize(["a", "b", "c", "e"], [
    (1,1,1,3),
    (0,0,0,0),
])
def test_solve_correctly(a,b,c,e):
    assert circumference(a,b,c) == e
    