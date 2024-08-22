# Instructions
# Write a Python program that prints the numbers from 1 to 100. If the number 
# is dividable by 3 print Fizz, if the number is dividable by 5 print Buzz 
# instead of the number. If the number is dividable by 3 and 5 print FizzBuzz 
# instead of the number.


# Add your code to the fizzbuzz() function.
# The function takes a number as an argument.
# If the number is evenly divisble by 3, the function returns "fizz"
# If the number is evenly divisble by 5, the function returns "buzz"
# If the number is evenly divisble by 3 and 5, the function returns "fizzbuzz"
# If the number is not evenly divisible by 3 or 5, the function returns the number.
def fizzbuzz(number : int=0) -> str:
    # TODO: add your code here
    return str(number)

# Add your code to the main() function.
# The main() function is run when the script is called from the command line.
# Loop through all numbers from 1 to 100 and call the fizzbuzz() funcion and
# print the result.
def main():
    # TODO: add your code here
    print(fizzbuzz())

if __name__ == "__main__":
    main()