import itertools
import operator

OPS = [operator.add, operator.sub, operator.mul, operator.truediv]


def arithmetic_outputs_run_length(digits):
    """Computes the consecutive run length in the arithmetic outputs of 4 digits.

    This method computes all possible positive integer outputs that can be obtained
    after applying the arithmetic operations (+. -, *, /) to the 4 given digits,
    and then computes the longest consecutive run from 1 to n in those outputs.

    Args:
        digits: List of 4 positive digits.
    Returns:
        Longest consecutive run length
    """
    assert len(digits) == 4, "There must be exactly 4 digits in the list"
    assert [0 <= d < 10 for d in digits], "All 4 elements must be single digit"
    assert [isinstance(d, int) for d in digits], "All elements must be integers"

    outputs = set()
    for a, b, c, d in itertools.permutations(digits):
        for op1, op2, op3 in itertools.product(OPS, repeat=3):
            result1 = op1(op2(op3(a, b), c), d)
            if result1 > 0 and float(result1).is_integer():
                outputs.add(result1)
            result2 = op1(op2(a, b), op3(c, d))
            if result2 > 0 and float(result2).is_integer():
                outputs.add(result2)

    # Computes the length of the consecutive run from 1 to n in the outputs.
    return next(i for i in itertools.count(1) if i not in outputs) - 1


print max(itertools.combinations(range(1, 10), 4), key=arithmetic_outputs_run_length)
