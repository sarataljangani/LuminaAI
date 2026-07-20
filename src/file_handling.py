# Writing to a file
with open("notes.txt", "w") as file:
    file.write("LuminaAI Day 3 Practice\n")
    file.write("Learning File Handling")

print("File created successfully!")

# Reading the file
with open("notes.txt", "r") as file:
    content = file.read()

print("\nContent of the file:")
print(content)