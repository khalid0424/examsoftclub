def find_min(lst):
    if len(lst) == 1:
        return lst[0]
   
    min_of_rest = find_min(lst[1:])
    return min(lst[0], min_of_rest)

input_list = list(map(int, input("lista vorid kun: ").split()))


result = find_min(input_list)

print(result)