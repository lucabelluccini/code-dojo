
class FizzBuzz:

    FIZZ = "Fizz"
    BUZZ = "Buzz"

    @staticmethod
    def fizzbuzz(number):
        fizz = FizzBuzz.FIZZ if number % 3 == 0 else ""
        buzz = FizzBuzz.BUZZ if number % 5 == 0 else ""
        output = fizz + buzz
        return output if output else str(number)
    
    @staticmethod
    def run(start=1, end=100):
        for num in xrange(start, end + 1):
            print FizzBuzz.fizzbuzz(num)

if __name__ == '__main__':
    FizzBuzz.run()