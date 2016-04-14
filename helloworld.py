from __future__ import print_function

number = input("Number: ")
myArray = []
i, count = 0, 0
for idx in range(number):
    myArray.append(0)
while i > -1:
    count += 1
    for j in myArray:
        print(j, end="")
    print ("\n", "")
    i = number - 1

    while i > -1:
        if myArray[i] == 0:
            myArray[i] = 1
            for idx in range(i + 1, number):
                myArray[idx] = 0
            break
        i -= 1
print("Generation count: ", count, "")
