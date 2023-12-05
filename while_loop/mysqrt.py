"""An algorithm that computes square root"""


def mysqrt(num: int) -> float:
    """Compute square root of a given number"""
    left, right = 1, num
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        m_squared = mid * mid

        if m_squared == num:
            return mid

        if m_squared < num:
            left = mid + 1
        else:
            right = mid - 1
    return mid


print(mysqrt(10))
