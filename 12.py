#Reverse a list

L=[1,2,3,4,5]

K=[]

for i in L:
    if i not in K:
        K.insert(0,i)
print(K)


