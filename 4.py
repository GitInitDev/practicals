odd = {x for x in range(0,10)}
prime = set()
for num in range (10,51) :
    if num > 1 :
        for i in range(2,num) :
            if num%i==0 :
                break
            else :
                prime.add(num)
print("Odd Numbers : ",odd)
print("Prime Numbers : ",prime)
print("Union : ",odd.union(prime))
print("Intersection : ",odd.intersection(prime))
print("Difference : ",odd.difference(prime))
print("Symmetric Difference : ",odd.symmetric_difference(prime))
