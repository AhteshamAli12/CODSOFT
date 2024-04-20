task = []

def add_task(task):
    task_number = int(input("\nEnter how many task you want to enter\n"))
    for i in range(0, task_number):
        new_task = input(f"Enter {i+1} task: ")
        task.append(new_task)


def show_list(task):
    if not task:
        print("\nNo Any task exist!\n")
    else:
        print("\nTo Do List\n")
        for i in range(0, len(task)):
            print(f"{i+1}.", task[i])

def delete_task(task):
    print("\nTo Do List\n")
    for i in range(0, len(task)):
        print(f"{i+1}.", task[i])
    task_del = int(input("Enter number of task to delete:"))
    if task_del > 0 and task_del <= len(task):
        task.pop(task_del-1)
    else:
        print("Invalid task number. No task deleted.")    

def update_task(task):
    if not task:
        print("\nNo Any task exist!\n")
        return
    else:
        print("\nTo Do List\n")
        for i in range(0, len(task)):
            print(f"{i+1}.", task[i])

        update_Task_num = int(input("Enter which task you want to update:"))
                    
        updatetask = input("Enter the updated task: ")
        for i in range(0, len(task)):
            if update_Task_num-1 == i:
                task[i] = updatetask


       
while True:
        print("\n~~~~~~~~~~~To Do list~~~~~~~~~~~\n")
        print("Select an option: ")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Update Task")
        print("4. delete Task")
        print("5. Save and Exist")
        x = input("Enter Option number: ")
        try:
            if int(x) == 1:
                show_list(task)
            elif int(x)==2 :
                add_task(task)
            elif int(x)==3 :
                update_task(task)
            elif int(x)== 4:
                delete_task(task)
            elif int(x) == 5:
                print("Exiting\n")
                break
            else:
                print("Envalid Option. Please Enter Valid integer!")
        except:
             print("Envalid Option. Please Enter Valid integer!")
