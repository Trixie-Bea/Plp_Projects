#file creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("My name is Beatrice\n")
        file.write("I like Python!\n")
        file.write("I was born in 2000\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
    
# file Reading and Display
try:
    with open("my_file.txt","r") as file:
        print("contents of my_file.txt")  
        content= file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")      

    
#file appending
try:
    with open("my_file.txt", "a") as file:
        file.write("I like watching movies.\n")
        file.write("I like to read books.\n")
        file.write("I also like the colour purple.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")   
    
    
    
    