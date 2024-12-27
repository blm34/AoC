from typing import Iterable
from functools import reduce


def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor using the Euclidean algorithm

    Args:
        a: The first number
        b: The second number

    Returns:
        The gcd of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(nums: Iterable[int]) -> int:
    """
    Calculates the lowest common multiple of an iterable of numbers

    Args:
        nums: Iterable of ints of which to find the lowest common multiple

    Returns:
        The lowest common multiple of the ints
    """
    ans = 1
    for num in nums:
        ans = ans // gcd(num, ans) * num
    return ans


def prod(nums: Iterable[int | float]) -> int | float:
    """
    Calculate the product of numbers in an iterable

    Args:
        nums: An iterable containing numbers

    Returns:
        The product of all numbers in nums
    """
    return reduce((lambda x, y: x * y), nums)


def digit_count(num: int) -> int:
    """
    Count the number of digits in a number

    Args:
        num: The number

    Returns:
        The number of digits in num
    """
    if num == 1:
        return 1

    d = 1
    while 10 ** d <= num:
        d *= 2

    min_d = d // 2
    max_d = d

    while min_d != max_d:
        mid_d = (min_d + max_d) // 2
        if 10 ** mid_d <= num:
            min_d = mid_d + 1
        else:
            max_d = mid_d

    return min_d
