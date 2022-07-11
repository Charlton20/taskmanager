
# Create a list for all the tasks and users
user_task = []
total_tasks = []
# Declare login details as false
login = False

# Open the user.txt file
f = open("user.txt", 'r')
for line in f:
    user_task.append(line.split())

while True:
    username = input("Enter your username: ")
    password = input('Enter your password: ')

    for i in range(len(user_task)):
        if username and password in user_task[i]:
            login = True

    if login == True:
        # Break out of the loop
        break
    else:
        print('Please Enter a valid username and password: ')
# Close the file
f.close()

# if the user inputs are valid, the program should run
while True:
    # print out the menu once login details are valid
    print('''
r - Register a user
a - Adding a task
va - View all tasks
vm - View my tasks
s - View statistics
e - Exit
''')

    userChoice = input(" : ")
    # Open the user.txt file
    f = open('user.txt', 'a+')

    # Display the menu inputs if user inputs the key "r"
    if userChoice == 'r':
        if username != "admin":
            print("Only admin can add new users.")
        elif username == 'admin':
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            confirm = input("Please confirm new password: ")
            if confirm == new_password:
                print("User registered successfully.")
                f.write(f'\n{new_username}, {new_password}')
            elif confirm != new_password:
                print("Incorrect password!")
    # Close the file
    f.close()

    # Display the input options if the user selects from the menu "a"
    if userChoice == "a":

        user_name = input("Enter username: ")
        task_title = input("Enter task title: ")
        task_description = input("Enter the description of the task: ")
        current_date = input("Enter the date the task was assigned: ")
        due_date = input("Enter the due date: ")
        complete = input("Is the task completed: ")

        # open the tasks file to add tasks when user inputs 'a'
        tasks = open("tasks.txt", 'a+')

        tasks.write(f'''{user_name}, {task_title}, {task_description}, {current_date}, {due_date}, {complete}''')
        #Close the file
        tasks.close()

    # Display the input options if user selects "va"
    elif userChoice == "va":
        # Open the tasks.txt file
        file = open('tasks.txt', 'r')
        lines = file.readlines()

        for i in lines:
            temp = i.strip()
            temp = temp.split(", ")
# Print out all the tasks in the format below
            print(f'''
Task:             {temp[1]}
Assigned To:      {temp[0]}
Date Assigned:    {temp[4]}
Due Date:         {temp[3]}
Task Complete?:   {temp[5]}
Task Description: 
{temp[2]}''')
        # Close the file
        file.close()

    # Display the input options if the user selects "vm"
    elif userChoice == "vm":
        # Open the tasks.txt file
        f = open("tasks.txt", 'r')
        lines = f.readlines()
        for x in lines:
            temp = x.strip()
            temp = temp.split(", ")
            if temp[0] == username:
                print(f''' 
Task:            {temp[1]}
Assigned To:     {temp[0]}
Date Assigned:   {temp[4]}
Due date:        {temp[3]}
Task Complete    {temp[5]}
Task Description:
{temp[2]}''')
        # Close the file
        f.close()

# They will get access to a different menu option if the username == admin
# Will be able to view the statistics of how many tasks and users are registered
    elif userChoice == "s":
        if username != "admin":
            print("Only admins may view statistics.")
        elif username == "admin":
            user_count = "user.txt"
            counting = 0
            with open('user.txt', 'r') as f:
                for line in f:
                    counting += 1
            print("The total users are: ", counting)

            # Create a function that counts the number of tasks in the file
            num_tasks = "tasks.txt"
            task_counting = 0

            # Open the tasks.txt file
            file = open('tasks.txt', 'r')
            for line in file:
                task_counting += 1
            # Print the total of tasks
            print("Total tasks are: ", task_counting)

    # Terminate the whole program if the user sekects "e" from the menu
    elif userChoice == "e":
        print('Terminating...')
        # Break out the loop
        break
