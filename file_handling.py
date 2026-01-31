import csv

# ---------- TXT FILE HANDLING ----------

try:
    # 1 & 2. Create and write to text file
    with open("userdata.txt", "w") as file:
        file.write("Name: Alice\n")
        file.write("Role: Python Intern\n")
        file.write("Company: ABC Tech\n")

    # 3. Read file contents
    with open("userdata.txt", "r") as file:
        print("Text File Contents:")
        print(file.read())

    # 4. Append data to file
    with open("userdata.txt", "a") as file:
        file.write("Status: Active\n")

except FileNotFoundError:
    print("File not found!")
except IOError:
    print("File handling error occurred!")

# ---------- CSV FILE HANDLING ----------

# 6. Create CSV file and write multiple rows
with open("students.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Header
    writer.writerow(["ID", "Name", "Course", "Marks"])

    # Rows
    writer.writerow([101, "Alice", "Python", 88])
    writer.writerow([102, "Bob", "Data Science", 90])
    writer.writerow([103, "Charlie", "Web Dev", 82])

# 8. Read CSV data
print("\nCSV File Contents:")
with open("students.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
