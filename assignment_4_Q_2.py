# Triple all number in given list 
sample_list=[1, 2, 3, 4, 5, 6, 7]

def triple_list(sample_list):
    return sample_list*3

result = list(map(triple_list,sample_list))
print("Result : ",result)
