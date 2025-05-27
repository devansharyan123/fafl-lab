import os

class DAC:
    def __init__(self):
        self.acl = {
            "alice": {"file1.txt": ["r", "w"]},
            "bob": {"file1.txt": ["r"]}
        }

    def check_access(self, user, file, operation):
        if user in self.acl and file in self.acl[user] and operation in self.acl[user][file]:
            try:
                if operation == "r":
                    with open(file, "r") as f:
                        content = f.read()
                        print(f"✅ Access granted: {user} can read {file}")
                        print("\nFile content:\n" + content)
                        os.system(f"notepad {file}")  # Opens file in Notepad (Windows)
                        return
                elif operation == "w":
                    with open(file, "a") as f:
                        f.write("\nAccessed by " + user)
                        print(f"✅ Access granted: {user} can write to {file}")
                        os.system(f"notepad {file}")  # Opens file in Notepad (Windows)
                        return
            except FileNotFoundError:
                print(f"❌ File '{file}' not found!")
                return
        print(f"❌ Access denied: {user} cannot {operation} {file}")

# Interactive User Input
if __name__ == "__main__":
    dac = DAC()

    user = input("Enter username: ")
    file = input("Enter filename: ")
    operation = input("Enter operation (r/w): ")

    dac.check_access(user, file, operation)
