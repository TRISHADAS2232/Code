t=("apple","banana","pinapple","cherry")
print("items in tuple:",t)
print("length of tuple:",len(t))
print("accessing an item:",t[1])
t1=list(t)
t1.append("berry")
print("items after append:",tuple(t1))
