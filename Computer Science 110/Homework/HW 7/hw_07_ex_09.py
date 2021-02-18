# hw_07_ex_09

def print_triangular_numbers(n):
    '''Print out the first n triangular numbers'''
    counter = 0
    for i in range(n):
        counter += 1
        tri_num = (1 + counter)*counter*.5 # Arithmetic sequence summation formula
        print(counter,"\t",int(tri_num))

# test
print_triangular_numbers(5)

##1 	 1
##2 	 3
##3 	 6
##4 	 10
##5 	 15
##>>> 
