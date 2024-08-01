from datetime import datetime

class Diary:
    def __init__(self, filename="diary.txt"):
        self.filename = filename

    def write_entry(self, entry):
        with open(self.filename, 'a') as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date} {entry}\n\n")

    def read_entries(self):
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No diary entries found")

diary = Diary()
while True:
    print("\n1. Write Entry\n2. Read Entries\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Write your diary entry: ")
        diary.write_entry(entry)
    elif choice == "2":
        diary.read_entries()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")