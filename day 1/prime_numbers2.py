def prime_numbers(): #defining function

    
    for num in range(0): #get numbers from zero to n
        if num > 1:
            for factor in range(2, num): #geting i to divide num with
                if (num % factor) == 0: #checks if number is prime by dividing with the other numbers
                    break
            else:
                print(num) #if above fails number is prime print it out


prime_numbers() #calling function
