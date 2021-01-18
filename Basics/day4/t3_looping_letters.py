full_name = 'Marina Suvorova'
number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0

for i in range(len(full_name)):
    if full_name[i] == "a":
        number_of_a += 1
    if full_name[i] == "e":
        number_of_e += 1
    if full_name[i] == "i":
        number_of_i += 1
    if full_name[i] == "o":
        number_of_o += 1
    if full_name[i] == "u":
        number_of_u += 1

total_letter = f'''
Total number of As: {number_of_a}
Total number of Es: {number_of_e}
Total number of Is: {number_of_i}
Total number of Os: {number_of_o} 
'''
print(total_letter)