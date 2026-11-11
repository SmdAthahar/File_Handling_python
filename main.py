# STEP 1: Create a file and write 10 lines

file = open("notes.txt", "w", encoding="utf-8")

file.write("Python is a programming language.\n")
file.write("Python is easy to learn.\n")
file.write("File handling is an important concept.\n")
file.write("We can create files using Python.\n")
file.write("We can read data from files.\n")
file.write("We can write data into files.\n")
file.write("We can append new data to files.\n")
file.write("Python supports different file modes.\n")
file.write("The read mode is represented by r.\n")
file.write("The write mode is represented by w.\n")

file.close()

print("File created and 10 lines written successfully!")


# STEP 2: Read the entire file

with open("notes.txt", "r", encoding="utf-8") as file:

    content = file.read()

    print("\n===== COMPLETE FILE CONTENTS =====")
    print(content)


# STEP 3: Read a specific number of characters

with open("notes.txt", "r", encoding="utf-8") as file:

    content = file.read(20)

    print("\n===== FIRST 20 CHARACTERS =====")
    print(content)


# STEP 4: Read only the first line

with open("notes.txt", "r", encoding="utf-8") as file:

    first_line = file.readline()

    print("\n===== FIRST LINE =====")
    print(first_line)


# STEP 5: Read all lines using readlines()

with open("notes.txt", "r", encoding="utf-8") as file:

    all_lines = file.readlines()

    print("\n===== ALL LINES USING READLINES =====")

    for line in all_lines:
        print(line.strip())


# STEP 6: Append additional notes

with open("notes.txt", "a", encoding="utf-8") as file:

    file.write("We can use the append mode to add new content.\n")
    file.write("The append mode is represented by a.\n")
    file.write("The close method closes an opened file.\n")
    file.write("With open automatically closes the file.\n")

print("\nAdditional notes appended successfully!")


# STEP 7: Reopen the file and display updated contents

with open("notes.txt", "r", encoding="utf-8") as file:

    updated_content = file.read()

    print("\n===== UPDATED FILE CONTENTS =====")
    print(updated_content)


# STEP 8: Demonstrate manual file closing

file = open("notes.txt", "r", encoding="utf-8")

print("\n===== MANUAL FILE CLOSING =====")
print("File opened:", not file.closed)

file.close()

print("File closed:", file.closed)


# STEP 9: Demonstrate automatic file closing

with open("notes.txt", "r", encoding="utf-8") as file:

    print("\n===== WITH OPEN DEMONSTRATION =====")
    print("File is currently open:", not file.closed)

print("File automatically closed:", file.closed)


print("\n===== FILE HANDLING DEMONSTRATION COMPLETED =====")