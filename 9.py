L=["apple","apple","banana"]
L1=[]
#count of unique elements

def unique_element_count(L):
    for i in L:
        if i not in L1:
            L1.append(i)
    return len(L1)

count=unique_element_count(L)

print("The unique element count:",count)