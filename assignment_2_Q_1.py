lst=[(5,0),(8,6),(7,5),(1,3),(4,1),(8,2),(9,4)]
leng = len(lst)
for i in range(0,leng):
    for j in range(0, leng-i-1):
        if (lst[j][1] > lst[j + 1][1]):
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
print(lst)