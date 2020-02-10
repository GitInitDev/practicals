import matplotlib.pyplot as plt
subjects = ["Language" , "English" , "Math" , "Science" , "Ethics"]
marks = [int(input("Enter Marks : ")) for i in range(1,6)]
for j in range(len(marks)) :
    print("{}.{} Mark = {}".format(j+1,subjects[j],marks[j]))
plt.title("MARKS")
plt.pie(marks , labels=subjects)
plt.axes().set_aspect("equal")
plt.show()
