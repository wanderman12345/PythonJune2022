# and - or - not
var_one = True
var_two = False

'''
AND truth table - and
R = S1 and S2 
S1  S2  R
T   T   T
T   F   F
F   T   F
F   F   F
'''

print(var_one and var_two)

'''
OR truth table - or
R = S1 or S2 
S1  S2  R
T   T   T
T   F   T
F   T   T
F   F   F
'''

print(var_one or var_two)

print(var_one, not var_one)