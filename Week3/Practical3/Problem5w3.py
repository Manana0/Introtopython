list5=[2,4,5,7,8,9,5,5,7]
print(list5)
notwanted=[0,4,5]
for i in sorted(notwanted, reverse=True): 
    del list5[i] 
print (list5) 