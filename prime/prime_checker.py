import sys
from math import sqrt

file_name = sys.argv[1]


def is_prime(n: int) -> bool:
    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False
    
    for m in range(5, int(sqrt(n))+1, 6):
        if n % m == 0 or n % (m + 2) ==0:
            return False
    


    return True


with open(file_name) as input_numbers:
    for line in input_numbers:
        number = int(line)
        print(1 if is_prime(number) else 0)
    
