list5=[2,4,5,7,8,9,5,5,7]
print(list5)
newlist5= list5.copy()
notwanted=[0,4,5]
for i in sorted(notwanted, reverse=True): 
    del newlist5[i] 
print (newlist5) 