#create a file.txt that 20 contains intergers 
#find the odd and even numbers and put it to a seperate file.txt
#and square the even numbers and cube the odd numbers

with open("intergers.txt", "r") as integer_file, open("squared.txt", "w") as squared_file, open("cubed.txt", "w") as cubed_file:
    for number in integer_file:
        if int(number) % 2 == 0:
            square = int(number) ** 2
            squared_file.write(square)
        else:
            cubed = int(number) ** 3
            cubed_file.write(cubed)
            