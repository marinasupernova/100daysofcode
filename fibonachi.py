'''def fib(quant):
    fib_numbers = [0, 1]
    i = 2

    #fib_numbers[2] = fib_numbers[0] + fib_numbers[1]

    while i < quant:
        new_element = fib_numbers[i-2] + fib_numbers[i-1] 
        fib_numbers.append(new_element)

        i += 1

    return fib_numbers


print(fib(30))



5 19 39 3 0 90 11300 6
'''



def change(text):
    output = []


    length = len(text)
    i = 0

    while i < length:
        if text[i] == ",":
            output.append(".")
        elif text[i] == ".":
            output.append(",")
        else:
            output.append(text[i])
        
        i+=1

    return ''.join(output) 


print(change("...1,2,3,4,5....."))
