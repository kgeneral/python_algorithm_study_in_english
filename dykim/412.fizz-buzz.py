class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fizz(i) + self.buzz(i) if i%3==0 or i%5==0 else str(i) for i in range(1, n+1)]
    
    def fizz(self, n: int) -> str:
        return "Fizz" if n % 3 == 0 else ""
    
    def buzz(self, n: int) -> str:
        return "Buzz" if n % 5 == 0 else ""
