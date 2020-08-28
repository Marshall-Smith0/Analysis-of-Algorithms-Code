##################################################################
# Student name: Marshall Smith 
# Course: COSC 3523 Analysis of Algroithms
# Assignment: #0: Insertion Sort
# Filename: smith0.py
#
# Purpose: The sort function should also come with a sample array that is initially unsorted. 
# You must implement the sort yourself. 
# For testing, use the following array: [100 95 31 45 44 58 29 92 12 17 42 12 5 1]
#
# Assumptions: None known
#
# Limitations: must implement the sort ourselves
#
# Development Computer: Windows 
# Operating System: Windows 
# Compiler: Python 3.7
# Integrated Development Environment (IDE): Visual Studio Code
# Operational Status:
###################################################################



def main():
    # Array that was give to us in the assignment 
    array = [100, 95, 31, 45, 44, 58, 29, 92, 12, 17, 42, 12, 5, 1]
    
    print("This is the unsorted array")
    print(array)
    
    # for loop to that will go through the whole array
    # start range at 1 otherwise it will go through and not hit the while loop at all and it will be a waste of a run 
    for i in range(1, len(array)):
        # sets key to the first point in the array
        key = array[i]
        # j is the pointer that goes through the array (start j = 0)(the first spot in the array)
        j = i - 1
        # This while loop will move elements in array that are greater then key one position ahead of the current spot
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        # updates key so that it will be able to check the next element in array
        array[j + 1] = key
    
    print("This is the sorted array")
    print(array)

if __name__ == "__main__":
    main()