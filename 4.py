L=[1,2,3,4,5,6] #unique
K=[1,2,2,3,3,4] #duplicate
def List_type(lst):
    return len(lst)==len(set(lst))

print(List_type(L))
print(List_type(K))