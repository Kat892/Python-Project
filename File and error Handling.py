try:
    file=open("Sample.txt","r+")
    writing_data=file.write("This is a sample text file")
    print(writing_data)
    file.close()

    file=open("Sample.txt","a")
    appending_data=file.write("\nIt contains multiple lines")
    print(appending_data)
    file.close()

    file=open("Sample.txt", "r")
    reading_data=file.read()
    print(reading_data)
    file.close()

except FileNotFoundError:
    print("The file Sample.txt was not found")

#FileNotFoundError: