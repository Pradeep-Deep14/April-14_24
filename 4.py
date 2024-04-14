list=[1,0,2,0,4,6]
for i in list:
    if i==0:
        list.remove(i)
        list.append(i)
print(list)

#remove it
#add the element in the last.