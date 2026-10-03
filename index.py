import os

tasks = []

while True:
    print("1. Save Paragraph")
    print("2. Save Task")
    print("3. Remove task")
    print("4. remove paragraph")
    print("5. See Paragraph")
    print("6. See tasks")
    print("7. Exit")

    user = input("Hi, what do you wanna like to do: ")

    if user == "1" or user == "save paragraph":
        para = input("Enter the paragraph you wanna save: ")
        with open("file1", "w") as f1:
            f1.write(para)
        print("Done")
    elif user == "2" or user == "save task":
        task = input("Enter the task you wanna save: ")
        tasks.append(task)
        print(f"Saved {task}")
    elif user == "3" or user == "remove task":
        rtask = input("Enter the task you wanna remove: ")
        tasks.remove(rtask)
        print(f"Removed {rtask}")
    elif user == "4" or user == "remove paragraph":
        os.remove("file1")
        print("Done")
    elif user == "5" or user == "see paragraph":
        try:
            if os.path.exists("file1"):
                with open("file1", "r") as r1:
                    rpara = r1.read()
                    print(rpara)
            else:
                print("No paragraph found.")
        except Exception as e:
            print(f"Error: {e}")
    elif user == "6" or user == "see tasks":
        if tasks:
            print(tasks)
        else:
            print("No tasks found.")
    elif user == "7" or user == "exit":
        break
    else:
        print("Option not available.")