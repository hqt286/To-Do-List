from Task import task # this is how you import a class from different file
from Task import DateAndTime
import shlex


def readTaskFile(inputfile):
    """ readTaskInput will take in a
    file name with the format
    "subject" "deadline date" "time" "completion hour" "note"
    in each line and store all of them inside an array.
    The function will return that array"    """
    task_list = list()
    with open(inputfile) as input:
        for line in input:
            line = line.strip()
            if len(line) > 0:
                line = shlex.split(line)
                eachTask = task()
                date = line[1].split('/')
                timing = line[2].split(':')

                time = DateAndTime()
                time.setTime(int(timing[0]), int(timing[1]),0, 
                int(date[0]), int(date[1]), int(date[2]))

                eachTask.newTask(time, str(line[0]), float(line[3]), str(line[4]))
                task_list.append(eachTask)

    return task_list



#in the future, we add more features to this file. for Ex:
#if the input file is not written is correct syntax or order, give out an error message
#allow different order of a file
#check every input to see if they are correct data or not