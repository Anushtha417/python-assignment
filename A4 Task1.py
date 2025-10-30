# Program to read a file and handle errors

try:
    # Try opening the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes extra newline characters

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occurred:", e)
