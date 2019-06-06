"""FizzBuzz Test"""

"""Write a program that prints the numbers from 1 to 100. But for multiples 
of three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
"""
for num in range(1,101):
    output1 = output2 = ""
    if not(num % 3):
        output1 = "Fuzz"
    if not(num % 5):
        output2 = "Buzz"
    output = output1 + output2
    if len(output) == 0:
        print(num)
    else:
        print(output)
