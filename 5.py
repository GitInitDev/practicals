import csv
with open('info.csv' , 'w') as f :
    w = csv.writer(f)
    for i in range(1,11) :
        name = input("Enter The Name : ")
        score = input("Enter The Strength Number : ")
        w.writerow([name,score])
print("Player File Created ...[]...")
f.close()
querySelector = input("Enter The Name To Be Searched : ")
f = open("info.csv" , 'r')
reader = csv.reader(f)
lst=[]
for row in reader :
    lst.append(row)
for row in lst :
    if querySelector in row :
        print(row)
    else :
        print("404 Not Found :(")
f.close()
