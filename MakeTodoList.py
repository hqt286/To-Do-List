from Task import task # this is how you import a class from different file
from Task import DateAndTime
from Task import oneDayTasks
from ReadTaskFile import readTaskFile
import datetime


def checkExpiredTask(Task, Today):
    if (Task.due_time.year < Today.year):
        return True
    if (Task.due_time.year == Today.year):
        if (Task.due_time.day < Today.day):
            return True
        if (Task.due_time.day == Today.day):
            if (Task.due_time.hour < Today.hour):
                return True
            if (Task.due_time.hour == Today.hour):
                if (Task.due_time.minute == Today.minute):
                    return True
    return False


def main():
    task_list = readTaskFile("taskList.txt")
    task_list.sort()
    listSize = len(task_list)
    dayNumber = 0
    allTodoList = list()

    i = 0
    # take out all the expired task
    while i < listSize:
        if checkExpiredTask(task_list[i], datetime.datetime.today()):
            del task_list[i]
        else:
            i = i + 1
        listSize = len (task_list)
    # organize task according to the day
    while listSize > 0:
        date = datetime.datetime.today() + datetime.timedelta(days=dayNumber)
        index = 0
        today_list = oneDayTasks()
        today_list.setDateTask(DateAndTime(date))

        while index < listSize:
            if (task_list[index].due_time.day == date.day
            and task_list[index].due_time.month == date.month
            and task_list[index].due_time.year == date.year):
                today_list.addTask(task_list[index])
                del task_list[index]
            else:
                index = index + 1
            listSize = len (task_list)
        
        while (today_list.timeAvailable() > 1 and listSize > 0 ):
            if (task_list[0].completion_TimeInHour < today_list.timeAvailable()):
                today_list.addTask(task_list[0])
                del task_list[0]
                listSize = len (task_list)
            else:
                firstPartTask = task(task_list[0])
                task_list[0].setTaskTime(task_list[0].completion_TimeInHour - today_list.timeAvailable())
                firstPartTask.setTaskTime(abs(today_list.timeAvailable() - task_list[0].completion_TimeInHour))
                today_list.addTask(firstPartTask)
                       
        dayNumber += 1
        allTodoList.append(today_list)

    output = open ("Your to do list.txt", "w+")

    for eachTodoList in allTodoList:
        output.write(eachTodoList.showDate())
        for eachTask in eachTodoList.taskList:
            output.write(eachTask.showTask() + "\n")
    output.close()
    print("Your to do list is sucessfully generated. Please check Your Your to do list.txt")

    
if __name__ == "__main__":
    main()