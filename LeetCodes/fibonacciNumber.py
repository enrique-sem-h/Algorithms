# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
