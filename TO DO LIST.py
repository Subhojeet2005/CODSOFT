userinput=[]
while True:
    print('1. ADD TASKS'+'\n'+ '2. SHOW TASK'+'\n'+'3. DELETE TASK'+'\n'+'4. QUIT')
    CHOICE=int(input('Choose an input option: '))
    if CHOICE==1:
        while True:
            user_input=input('Please enter your prompt , ( enter q for quiting): ')
            if user_input=='q':
                break
            userinput.append(user_input)
    elif CHOICE==2:
        if userinput:
            import pandas as pd
            INPUT=pd.Series(userinput,index=range(1,len(userinput)+1))
            print(INPUT)
        else:
            print('No tasks to show')
    elif CHOICE==3:
        if userinput:
            print("Current tasks:")
            for i, task in enumerate(userinput, 1):
                print(f"{i}. {task}")
            task_number=int(input('Enter task number to delete: '))
            if 1 <= task_number <= len(userinput):
                del userinput[task_number - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")
    elif CHOICE==4:
        print('Thank you for using the task manager')
        break 
    else:
        print('Invalid input')
        