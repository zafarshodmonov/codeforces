import pytest

from contest import Contest_27_06_2024
from input_output_A import A, InputFunction, OutputFunction
from problemset import CodeForces

input_function = InputFunction()
output_function = OutputFunction()

ans = A("71A", 1, input_function.F71A, output_function.F71A)
    
codeforces = CodeForces()

@pytest.mark.parametrize(
        "words, out",
        ans
)
def test_leetcode(words, out):
    assert codeforces.F71A_processing(words) == out