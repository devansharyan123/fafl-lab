import os

class MAC:
    def __init__(self):
        self.clearance = {
            "alice": 3,
            "bob": 2
        }
        self.file_labels = {
            "file1.txt": 2,
            "file2.txt": 3
        }

    def check_access(self, user, file):
        if user in self.clearance and file in self.file_labels:
            if self.clearance[user] >= self.file_labels[file]:  # User clearance must be >= file label
                try:
                    with open(file, "r") as f:
                        content = f.read()
                        print(f"✅ Access granted: {user} can read {file}")
                        print("\nFile Content:\n" + content)
                        os.system(f"notepad {file}")  # Opens file in Notepad (Windows)
                        return
                except FileNotFoundError:
                    print(f"❌ File '{file}' not found")
                    return
            else:
                print(f"❌ Access denied: {user} does not have a high enough clearance to access {file}")
                return
        print(f"❌ Access denied: Invalid user or file")

if __name__ == "__main__":
    mac = MAC()

    user = input("Enter username: ")
    file = input("Enter filename: ")

    mac.check_access(user, file)
