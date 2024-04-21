#create a file named(number.txt) 
#write a code that seperates the odd and even numbers to a different file

with open("numbers.txt", "r") as my_file, open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:
    for number in my_file:
        if int(number) % 2 == 0:
            even_file.write(number)
        else:
            odd_file.write(number)
            