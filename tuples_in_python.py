#Tuples in Python

L = [100, 200, 300]

T = (100, 200, 300)

L.append(400)
# T.append(400) <- This won't work because tuples are immutable unlike lists.

print("List L =",L,"<- L.append(400) works")
print("Tuple T = ",T,"<- T.append(400) won't work")