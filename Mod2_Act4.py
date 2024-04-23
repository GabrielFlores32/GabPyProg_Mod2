#write a program that is like a diary
#all off the output must be in a file named "mylife.txt"

def input_lines():
    resume = True
    while resume:
        line = input("Enter line: ")
        enter_line = line + ("\n")
        with open("mylife.txt", "a") as mylife_file:
            mylife_file.write(enter_line)
            
        
