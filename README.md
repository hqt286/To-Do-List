What Can This Software Do ? 

Maketo doList.py is a piece of python that helps the user to organize their to do task in an efficient way.
The software will take in data from a file called taskList.txt and organzie them. Each day, the program will assume the user work for 12 hours. Therefore, each day to do list will contain only the amount of work that user could do in 12 hours. For example, if user enter 2 different tasks and each task would take 8 hours, the program will add the first task to the list then break the second task into 2 sub task. The first subtask will be added to one day to do list, and the second subtask will be added to next day to do list. If there is 
any expired task, the program will take it off the todo list every time the user generate a new todo list. 

How to use the program ? 

    Put these 4 files inside the same directory.
    ReadTaskFile.py
    MaketodoList.py
    Task.py
    taskList.txt

    Go into taskList.txt file to add your task follow this format
     "Class Number"  "deadline (mm/dd/yyyy)"  "due time (hh:mm)"  "amount of time to complete the assignment in hours" "note for the assignment"
    For example:
     "ECE3115"       "12/20/2018"	"21:22"	"0.5"   "do HW 1 2 3 4"

    IMPORTANT RULES:
     Each string has to go between quotation mark ("").
     The order is important. User has to follow above order.
     Each task must be represent in 1 line.
     Make sure the date and time are correct.
     Each task completion time has to be less than 12 hours.

    Once the user enter the all the task with all the due date, open the terminal, go to the file directory and type the command
    
    python .\MaketodoList.py

    The user will see a new file create called "Your to do list.txt" located in the same directory.

    Check "Your to do list.txt" and see what tasks you have to do for today. 
