import pytest

from contest import Contest_27_06_2024
from problemset import CodeForces
from input_output_A import InputFunction, OutputFunction, A


input_function = InputFunction()
output_function = OutputFunction()

ans = A("116A", 2, input_function.F116A, output_function.F116A)
    
codeforces = CodeForces()

@pytest.mark.parametrize(
        "nums, out",
        ans
)
def test_leetcode(nums, out):
    assert codeforces.F116A_processing(nums) == out