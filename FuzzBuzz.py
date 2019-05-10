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
