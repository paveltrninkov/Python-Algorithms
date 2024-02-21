unsorted = [1,5,1,4,8,9,3,6,5,4,7,8]

#Bubble sort algorithm
def BubbleSort(array):
    #swap true to keep track if array is still being sorted
    swap = True
    while swap:
        #turn swap false to end loops if sorted
        swap = False
        #loop array to sort (iteration)
        for x in range(len(array)-1):
            if array[x] > array[x + 1]:
                #if greater than, swap places
                array[x], array[x + 1] = array[x + 1], array[x]
                #update swap check back to true and continue iterating
                swap = True
    #finally print sorted array
    print(array)

# BubbleSort(unsorted)

#Selection Sort algorithm
def SelectionSort(array):
    # marker for where sort starts in array
    marker = 0
    while marker < len(array):
        # loop through array starting from marker
        for x in range(marker, len(array)):
            # check values and switch
            if array[x] < array[marker]:
                array[marker], array[x] = array[x], array[marker]
        marker +=1
    print(array)
        

#SelectionSort(unsorted)

def InsertionSort(array):
    #first loop
    for x in range(1, len(array)):
        #key for comparison value
        key = array[x]
        #position to compare
        y = x - 1
        #while the value is greater than values, swap places
        while y >= 0 and key < array[y]:
            #keep swapping
            array[y + 1] = array[y]
            y -= 1
            array[y + 1] = key
    print(array)
            
#InsertionSort(unsorted)


def QuickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]
        smaller, equal, larger = [], [], []
        for i in array:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                larger.append(i)
        return QuickSort(smaller) + equal + QuickSort(larger)

print(QuickSort(unsorted))