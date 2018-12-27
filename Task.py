import calendar

class DateAndTime:
    """ 
    this class help the user store date time 
    """
    def __init__(self, other = None): # this is how you set up default constructor and copy constructor
        if (other is None):
            self.default_constructor()
        else:
            self.copy_constructor(other)

    def default_constructor(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.day = 1
        self.month = 1
        self.year = 1990

    def copy_constructor(self, other):
        self.hour = other.hour
        self.minute = other.minute
        self.second = other.second
        self.day = other.day
        self.month = other.month
        self.year = other.year

    def setTime(self, hour, minute, second, month, day, year):
        if (hour >= 0 and hour < 24):
            self.hour = hour
        if (minute >=0 and minute < 60):
            self.minute = minute
        if (second >=0 and second < 60):
            self.second = second
        if (day > 0 and day < 32):
            self.day = day
        if (month > 0 and month < 13):
            self.month = month
        self.year = year

    def __eq__ (self, other):
        return (self.year == other.year and self.month == other.month 
        and self.day == other.day and self.hour == other.hour and 
        self.minute == other.minute and self.second == other.second)

    def __gt__ (self, other):
        """
        the LHS will be less important than the RHS
        if the assignment of LHS due the day after RHS assignment
        """
        if (self.year > other.year): 
            return True            
        if  (self.year == other.year):
            if (self.month > other.month):
                return True
            if (self.month == other.month):
                if (self.day > other.day):
                    return True
                if (self.day == other.day):
                    if (self.hour > other.hour):
                        return True
                    if (self.hour == other.hour):
                        if (self.minute > other.minute):
                            return True
                        if (self.minute == other.minute):
                            if (self.second > other.second):
                                return True
        return False

    def __lt__ (self, other):
        """
        the LHS will be more important than the RHS
        if the assignment of LHS due the day before RHS assignment
        """
        if (self.year < other.year): 
            return True            
        if  (self.year == other.year):
            if (self.month < other.month):
                return True
            if (self.month == other.month):
                if (self.day < other.day):
                    return True
                if (self.day == other.day):
                    if (self.hour < other.hour):
                        return True
                    if (self.hour == other.hour):
                        if (self.minute < other.minute):
                            return True
                        if (self.minute == other.minute):
                            if (self.second < other.second):
                                return True
        return False


    def showTime(self):
        return (calendar.month_name[self.month] + " " + str(self.day) +", " + str(self.year) 
        + ' at\n' + str(self.hour) + ':' + str(self.minute) + ':' + str(self.second) + "\n")


class task:
    """
    this class help the user store each task.
    there will be deadline, subject, completion time,
    and note of the task contain in this object
    """
    def __init__(self, other = None):
        if (other is None):
            self.default_constructor()
        else:
            self.copy_constructor(other)

    def default_constructor(self):
        self.due_time = DateAndTime()
        self.subject = ""
        self.completion_TimeInHour = 0
        self.note = ""

    def copy_constructor(self, other):

        self.due_time = other.due_time
        self.subject = other.subject
        self.completion_TimeInHour = other.completion_TimeInHour
        self.note = other.note

    def newTask(self, deadline, subject, hours, note):
        self.due_time = deadline
        self.subject = subject
        self.completion_TimeInHour = hours
        self.note = note

    def showTask(self):
        return  ("Deadline of " + self.subject + " is" + "\n" + self.due_time.showTime() +       
        "The task will take " + str(round(abs(self.completion_TimeInHour),3))+ " hour(s) to complete"
        "\nNote:" + self.note + '\n')
    
    def setDeadline(self, deadline):
        self.due_time = deadline

    def setSubject(self, subject):
        self.subject = subject

    def setTaskTime(self, hour):
        self.completion_TimeInHour = hour

    def setNote(self, note):
        self.note = note

    def __eq__ (self, other):
        return (self.due_time == other.due_time
        and self.completion_TimeInHour == other.completion_TimeInHour)

    def __lt__ (self, other):
        """
        if the dead line is closer, the LHS task is less important than RHS task.
        if the dead line is same time, the task take less time will be less important
        than the task take more time
        """
        if (self.due_time > other.due_time):
            return False
        if (self.due_time == other.due_time):
            if(self.completion_TimeInHour > other.completion_TimeInHour):
                return False
        return True

    def __gt__ (self, other):
        """
        if the dead line is closer, the LHS task is more important than RHS task.
        if the dead line is same time, the task take less time will be more important
        than the task take more time
        """
        if (self.due_time < other.due_time):
            return False
        if (self.due_time == other.due_time):
            if(self.completion_TimeInHour < other.completion_TimeInHour):
                return False
        return True

class oneDayTasks:
    """
    this class is a list that contain all the
    task of one day.
    """
    def __init__ (self, other = None):
        if (other is None):
            self.default_constructor()
        else:
            self.copy_constructor(other)

    def default_constructor(self):
        self.DateAndTime = DateAndTime()
        self.taskList = list()

    def copy_constructor(self, other):
        self.DateAndTime = other.datetime
        self.taskList = other.taskList

    def addTask(self, Task):
        self.taskList.append(Task)

    def setDateTask(self, datetime):
        self.DateAndTime = datetime

    def showDate(self):
        return("***************************************************" + "\n"
           + "\t\t\t\t" "To do list " + str(self.DateAndTime.month) + "-" + 
        str(self.DateAndTime.day) + "-" + str(self.DateAndTime.year) + "\n"
        +"***************************************************" + "\n")
    
    def timeAvailable(self):
        """
        Assume there is 12 working hours each day
        this function will return the amount of working time
        left after complete all the todo task for this day.
        """
        busytime = 0
        for eachTask in self.taskList:
            busytime = busytime + eachTask.completion_TimeInHour

        return (12 - busytime)

