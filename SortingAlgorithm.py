from Task import task # this is how you import a class from different file

def merge(TaskList, first_Index, mid_Index, last_Index):
    first1 = first_Index
    last1 = mid_Index
    first2 = mid_Index + 1
    last2 = last_Index
    tempList = list()
    index = first1
    while (first1 <= last1 and first2 <= last2):
        if (TaskList[first1] <= TaskList[first2]):
            tempList[index] = TaskList[first1]
            first1 = first1 + 1
        else:
            tempList[index] = TaskList[first2]
            first2 = first2 + 1
        index = index + 1

    while (first1 <= last1):
        tempList[index] = TaskList[first1]
        index = index + 1

        TaskList = list(tempList)

def mergeSort(TaskList, first_Index, last_Index):
    """ merge sort is used to sort the task list 
        into ascending order. The most important 
        task will go first and the least important
        task will go after
    """
    if (first_Index < last_Index):
        mid_Index = last_Index/2
        mergeSort(TaskList, first_Index, mid_Index)
        mergeSort(TaskList, mid_Index + 1, last_Index)
        merge(TaskList, first_Index, mid_Index, last_Index)
    


