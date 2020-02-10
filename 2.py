n = int(input("Enter The Number : "))
def oddchk (num=n) :
    if n%2==0 :
        print(n, "Is Even")
    else :
        print(n, "Is Odd")
oddchk()
s = input("Enter The String To Reversed : ")
print("The Reverse Of {} Is {}".format(s,s[::-1]))
