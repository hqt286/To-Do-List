Hung Tran
ECE 2524

********************************** What Can This Software Do ? ********************************
***********************************************************************************************
    Maketo doList.py is a piece of python that help the user organize their to do task in an efficient way.
The software will take in data from a file called taskList.txt and organzie them. Each day, the program
will assume the user work for 12 hours. Therefore, each day to do list will contain only the amount
of work that user could do in 12 hours. For example, if user enter 2 different tasks and each task would take 8 hours,
the program will add the first task to the list then break the second task into 2 sub task. The first subtask 
will be added to one day to do list, and the second subtask will be added to next day to do list. If there is 
any expired task, the program will take it off the todo list every time the user generate a new todo list. 

********************************** How to use the program ? **************************************
**************************************************************************************************
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


********************************** How the software was written ? ********************************
**************************************************************************************************
    There are total 3 files in this software: 
    The first file called Task.py. This file contain code for 3 
different classes. The first class is "DateAndTime" which contain the data of time. The user can input
hour, minute, second, month, day, year into this DateAndTime object. The second class is "task". This object store
subject, dead line time (DateAndTime), note, and the amount of time to complete the project. One day task is the third
object. It contains all the tasks that the user has to do on that one day.
    The second file called ReadTaskFile.py. This file has one job is to read the file taskList.txt, parse 
all the information and save them into a list. There is only one function inside this file. The function 
will return a unsorted list of all the task. 
    The third file is MaketodoList.py. This is the main file that use all other file to soft each task 
into the right order of time. It will assign appropriate task per each day and also divide all the task
to all the day evenly. It start to check all the task that due today. Then add them into the to do list. If there 
is still time avalable of the day (if all the task due today takes less then 12 hours), it will look at more task 
and add them in in order to fill up 11-12 hours of work per day. If the task is too long, it also break the task 
down to sub parts and assign them in different day.
    The last file called taskList.txt. User can enter all their subject assignment following the format below.
    "Class Number"  "due date"  "due time"  "amount of time to complete the assignment" "note for the assignment"
    Once the program run, it will generate a file called "Your to do List". You can see what task you need to do for 
which day. 



