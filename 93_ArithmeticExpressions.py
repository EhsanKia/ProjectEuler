import itertools
import operator

OPS = [operator.add, operator.sub, operator.mul, operator.truediv]


def arithmetic_outputs(digits):
    """Computes all possible outputs applying arithmetic operations to 4 digits.

    Args:
        digits: List of 4 positive digits.
    Returns:
        Set of all possible positive integer outputs from arithmetic operations.
    """
    assert len(digits) == 4, "There must be exactly 4 digits in the list"
    assert [0 <= d < 10 for d in digits], "All 4 elements must be single digit"
    assert [isinstance(d, int) for d in digits], "All elements must be integers"

    outputs = set()
    for a, b, c, d in itertools.permutations(digits):
        for op1, op2, op3 in itertools.product(OPS, repeat=3):
            result1 = op1(op2(op3(a, b), c), d)
            if result1 > 0 and result1 % 1 == 0:
                outputs.add(result1)
            result2 = op1(op2(a, b), op3(c, d))
            if result2 > 0 and result2 % 1 == 0:
                outputs.add(result2)
    return outputs


def consecutive_run_length(nums):
    """Returns the length of the consecutive run from 1 to n in a list of ints."""
    return next(i for i in itertools.count(1) if i not in nums) - 1


# Define a function that finds all outputs and calculates the longest length.
longest_arithmetic_length = lambda x: consecutive_run_length(arithmetic_outputs(x))

print max(itertools.combinations(range(1, 10), 4), key=longest_arithmetic_length)
