def fibonacci_seq(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)


def e_gcd(a, b):
    if b == 0:
        return a
    else:
        return e_gcd(b, a % b)

def compare_string(s1, s2):
    if s1 == "" and s2 == "":
        return 0
    elif s1 == "":
        return -1
    elif s2 == "":
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compare_string(s1[1:], s2[1:])
