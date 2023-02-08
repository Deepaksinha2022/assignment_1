# Square all the elements of the list 

sample_list=[4, 5, 2, 9]

def square_list(sample_list):
    return sample_list ** 2

result = list(map(square_list,sample_list))

print(" Input list : ",sample_list)
print("Output list : ",result)