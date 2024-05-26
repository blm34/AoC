from typing import Iterable
from numpy import prod as product


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



def prod(nums: Iterable[int | float]):
    """
    Calculate the product of numbers in an iterable

    Args:
        nums: An iterable containing numbers

    Returns:
        The product of all numbers in nums
    """
    return product(nums)
