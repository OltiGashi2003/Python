#Die Fibonacci-Folge: f(n) = f(n-1) + f(n-2)  - first version
from functools import lru_cache
from typing import Dict, Generator

def fibonnaci(n: int):
    if n < 2:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)

if __name__ == "__main__":
    print(fibonnaci(5))
    print(fibonnaci(10))

# Die Fibonacci - Folge. Meomisation - Version - second version



memo: Dict[int, int] = {0: 0, 1: 1}

def fibonnaci_dict(n: int):
    if n not in memo:
        memo[n] = fibonnaci_dict(n-1) + fibonnaci_dict(n-2)
    return memo[n]

if __name__ == "__main__":
    print(fibonnaci_dict(5))
    print(fibonnaci_dict(50))

# Die Fibonacci - Folge mit Automatische Memooisation decorator - third version
# das ist auch die Fortschrittlich Methode Fibonacci 

@lru_cache(maxsize=None)
def fib4(n: int):
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)
if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
    

# Fibonacci leicht gemacht
def fib5(n: int):
    if n == 0: return n 
    last: int = 0 
    next: int = 1
    for _ in range(1, n):
        last, next = next, next + last
    return next
if __name__ == "__main__":
    print(fib5(6))
    print(fib5(50))

# Fibonacci-Zahlen mit einem Generator erzeugen

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next    
if __name__ == "__main__":
    for i in fibonacci_gen(50):
        print(i)
        
    