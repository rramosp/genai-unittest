
import math
import numpy as np


def isprime(number):
  if number <= 1:
    return False

  if number == 2:
    return True

  if number % 2 == 0:
    return False

  try:
      limit = math.isqrt(number)
  except AttributeError:
      limit = int(math.sqrt(number))

  for i in range(3, limit + 1, 2): # Check only odd numbers from 3 upwards
    if number % i == 0:
      return False # Found a divisor, so it's not prime

  return True


def cauchy(x, y):
    r = np.subtract.outer(x, y) 
    if np.sum(r==0)>0:
        raise ValueError("division by zero")
        
    return 1/r


def change_money(n):
    """
    given n, a number of cents between 1 and 99
    computes the number of coins of 1c, 10c and 25c to reach n
    """
    change=[0,0,0]
    if (n<1 or n>99):
        return None
    
    else:
        change[2]=n//25
        n-=change[2]*25
        change[1]=n//10
        change[0]=n%10
        return change