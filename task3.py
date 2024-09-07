def string_mo(given_string):
    def jam():
        return f"Salom {given_string}"
    return jam

input_string = input("Kalimai lozimiro vorid kuned: ")  


concat = string_mo(input_string)


result = concat()
print(result)