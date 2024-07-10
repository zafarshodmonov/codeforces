import pytest

from contest import Contest_27_06_2024
from input_output_A import A, InputFunction, OutputFunction
from problemset import CodeForces

input_function = InputFunction()
output_function = OutputFunction()

ans = A("231A", 1, input_function.F231A, output_function.F231A)
    
codeforces = CodeForces()

@pytest.mark.parametrize(
        "nums, out",
        ans
)
def test_leetcode(nums, out):
    assert codeforces.F231A_processing(nums) == out