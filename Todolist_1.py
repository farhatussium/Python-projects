todo=[]
while True:
    action=input("Add/view/quit?").lower()
    if action=="add":
        todo.append(input("Enter a task: "))
    elif action=="view":
        print("\nTasks:", todo if todo else "No tasks added yet.")
    elif action=="quit":
        break