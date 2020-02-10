num = [x for x in range(1,11)]
print("The List Befor Removal Of Odd Numbers Is : ",num)
for j,i in enumerate(num) :
    if i%2!=0 :
        del num[j]
print("The List After The Deletion Of Odd Numbers Is : ",num)
