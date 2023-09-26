target_num = int(input().split()[1])
mylist = list(map(int, input().split()))
mysum = 0
for i in range(len(mylist) - 2):
    for j in range(i + 1, len(mylist) - 1):
        for k in range(j + 1, len(mylist)):
            currentsum = mylist[i] + mylist[j] + mylist[k]
            if currentsum <= target_num and currentsum > mysum:
                mysum = currentsum
print(mysum)