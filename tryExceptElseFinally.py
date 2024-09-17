import time
#It is similar to an if statement, tries to catch known errors, if any arise, then the dedicated except state come to play
try:
    file = open("abc.txt")
    my_dict = {"name":"raja"}
    # key = "raja"
    # print(my_dict[key])

except FileNotFoundError:

    print("file does not exist. creating the file now\n")
    time.sleep(10)
    file = open("abc.txt", "w")

# except KeyError:
    # my_dict[key] = f"{key} does not exist, make sure to edit this."
    # print(f"{my_dict[key]}")
#else it will follow try block, if there are no erros and try block executes successfuly, else will run
#try implies else

else:
    print("The File opened")

#runs no matter what,

finally:
    file.close()
    print("The File Closed.")