def readInput(file):
    with open(f'{file}', 'r') as file:
        text = file.read().strip()
    return text

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(nums):
    ans = 1
    for num in nums:
        ans = ans // gcd(num, ans) * num
    return ans
