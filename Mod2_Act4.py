#write a program that is like a diary
#all off the output must be in a file named "mylife.txt"

def input_lines():
    resume = True
    while resume:
        line = input("Enter line: ")
        enter_line = line + ("\n")
        with open("mylife.txt", "a") as mylife_file:
            mylife_file.write(enter_line)
            while resume:
                questions = input("Are there more lines y/n? ")
                if questions.lower() == "y":
                    break
                elif questions.lower() == "n":
                    print("say less")
                    resume = False                   
                else:
                    print("Answer is invalid, use y/n only") 
                    continue
input_lines()              

        
