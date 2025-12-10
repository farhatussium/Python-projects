tasks=[] # list to store tasks  
while True:
    print("\n----TO-DO LIST MENU----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")


    choice=input("Enter your choice (1-4):")
    
    if choice=="1":
        #Add Task
        task=input("Enter the task to add:")
        tasks.append(task)
        print(" Task added.")
    elif choice=="2":
        #View Tasks
        if len(tasks)==0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice=="3":
        #Remove Task
        if len(tasks)==0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            
                task_num=input("Enter the task number to remove:")
                #Validate input
                if task_num.isdigit():
                    task_num=int(task_num)
                    if 1<=task_num<=len(tasks):
                        tasks.pop(task_num-1)
                        print("Task removed.")
                else:
                    print("Invalid task number.")  
    elif choice=="4":
        #Quit
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 to 4.")