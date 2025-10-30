# Step 1: Take user input and write it to a file
text = input("Enter some text to write to the file: ")

# Open file in write mode (this will create or overwrite the file)
with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data written to output.txt successfully!")

# Step 2: Take more input and append it to the same file
more_text = input("Enter additional text to append: ")

# Open file in append mode
with open("output.txt", "a") as file:
    file.write(more_text + "\n")

print("Additional data appended successfully!")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
