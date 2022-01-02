
def readFiles():
    file1_name = input("Enter the file1 name: ")
    file2_name = input("Enter the file2 name: ")

    file1 = open(file1_name, "r")
    file2 = open(file2_name, "r")

    file1_content = file1.read()
    file2_content = file2.read()

    file1.close()
    file2.close()

    return file1_content, file2_content