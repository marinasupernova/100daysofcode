
has_zero_legs = 0
has_two_legs = 0
has_four_legs = 0
leg_count = [4, 0, 2, 4, 2, 0, 2, 4, 4, 2, 0, 2, 4]
for i in range(len(leg_count)):
    if leg_count[i] == 0:
        has_zero_legs += 1
    if leg_count[i] == 2:
        has_two_legs += 1
    if  leg_count[i] == 4:
        has_four_legs += 1

total_legs = f'''
Animals with no legs: {has_zero_legs}
Animals with two legs: {has_two_legs}
Animals with four legs: {has_four_legs}
'''
print(total_legs) 