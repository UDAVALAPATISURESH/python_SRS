def file_read():
    file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example1.txt", "w")
    content = file.read()
    file.close()
    return content
    
# cont = file_read()
# print(cont)

# file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()

file = open(r"C:\Users\sisek\PycharmProjects\pythonProject\file handling\example1.txt", "a")
content = file.write("\n Africa")
print(content)