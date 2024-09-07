def sum_of_series(N):
    sum_result = 1  
    factorial = 1   
      
    for i in range(1, N + 1):
        factorial *= i 
        sum_result += 1 / factorial  
    
    return sum_result


N = int(input("дохил намоед: "))


result = sum_of_series(N)
print(f"{result:}")  
