num = int(input("Enter The Number To Calculate Factorial : "))
if num==0 :
    fact = 1
fact=1
for i in range(1,num+1) :
    fact = fact*i
print("Factorial Of {} Is {}".format(num,fact))
n = int(input("Enter The Value Of Last Number : "))
s = 0
for i in range(1,n+1) :
    a = (i**i)/i
    s = s+a
print("The Sum Of The Series Is : " ,s)
