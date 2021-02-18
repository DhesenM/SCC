# hw_05_ex_12

def is_rightangled(l1,l2,l3,):
    '''Return True if the triangle is right-angled, or False otherwise'''
    condition1 = abs(l1**2 + l2**2 - l3**2) < 0.000001
    condition2 = abs(l1**2 + l3**2 - l2**2) < 0.000001
    condition3 = abs(l2**2 + l3**2 - l1**2) < 0.000001
    
    if condition1 or condition2 or condition3:
        return True
    else:
        return False

# test
print(is_rightangled(3,4,5))
print(is_rightangled(4,4,5))
print(is_rightangled(5*2**.5,5,5))
print(is_rightangled(5,5*2**.5,5))

##True
##False
##True
##True
##>>> 
