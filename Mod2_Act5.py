#create a file.txt that 20 contains intergers 
#find the odd and even numbers and put it to a seperate file.txt
#and square the even numbers and cube the odd numbers

with open("integers.txt", "r") as integer_file, open("squared.txt", "w") as squared_file, open("cubed.txt", "w") as cubed_file:
    for number in integer_file:
        value = int(number)
        if value % 2 == 0:
            square = value ** 2
            squared_file.write(str(square)+"\n")
        else:
            cubed = value ** 3
            cubed_file.write(str(cubed)+"\n")
            