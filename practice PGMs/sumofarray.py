onearray = [1,2,3,4,5]
print(sum(onearray,5))

print(min(onearray))
print(max(onearray))

max = onearray[0]
n=len(onearray)

for i in range(1,n):
    if onearray[i]>max:
        max = onearray[i]
print(max)




