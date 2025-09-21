# Simple To-Do Application in Python

todos = []

def show_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add To-Do")
    print("2. View To-Do List")
    print("3. Delete To-Do")
    print("4. Delete All To-Dos")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter To-Do Title: ")
        date = input("Enter Date (dd-mm-yyyy): ")
        todos.append({"title": title, "date": date})
        print("✅ To-Do added successfully!")

    elif choice == "2":
        if len(todos) == 0:
            print("📭 No To-Do items found.")
        else:
            print("\nYour To-Do List:")
            for i, todo in enumerate(todos, start=1):
                print(f"{i}. {todo['title']} (Date: {todo['date']})")

    elif choice == "3":
        if len(todos) == 0:
            print("📭 No To-Do items to delete.")
        else:
            num = int(input("Enter To-Do number to delete: "))
            if 1 <= num <= len(todos):
                deleted = todos.pop(num-1)
                print(f"🗑️ Deleted: {deleted['title']}")
            else:
                print("❌ Invalid number!")

    elif choice == "4":
        todos.clear()
        print("🗑️ All To-Dos deleted!")

    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again.")
