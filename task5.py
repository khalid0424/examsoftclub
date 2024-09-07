def sum_of_squares(n):

    if n == 1:
        return 1
    else:
        
        return n**2 + sum_of_squares(n - 1)


n = int(input("Enter a natural number n: "))


result = sum_of_squares(n)
print(result)