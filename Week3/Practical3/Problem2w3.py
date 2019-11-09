import sys
list1= ["Hello", 1, True]
newlist1= list1.copy()
newlist1.append(sys.argv[1:])
print ("Old list:",list1)
print ("New list:", newlist1)