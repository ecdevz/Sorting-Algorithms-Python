## IMPORTING MODULES
import os
import time as Time
## DEFINE COLORS
colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "none": "\033[0m"
}
##********************** FUNCTIONS TO SORTING ALGORITHMS **********************##



# Bubble Sort Algorithm
def bubbleSort(inputArray, ascender = True):
    x = len(inputArray) 
    for y in range(x):
        for z in range(x - 1 - y):
            if ascender:
                if inputArray[z] > inputArray[z + 1]:
                    inputArray[z], inputArray[z + 1] = inputArray[z + 1], inputArray[z]
            else:
                if inputArray[z] < inputArray[z + 1]:
                    inputArray[z], inputArray[z + 1] = inputArray[z + 1], inputArray[z]
    return inputArray


# selection sort algorithm
def selectionSort(inputArray, ascender = True):
    for x in range(len(inputArray)):
        valueIndex = x
        for y in range(x + 1, len(inputArray)):
            if ascender:
                if inputArray[valueIndex] > inputArray[y]:
                    valueIndex = y
            else:
                if inputArray[valueIndex] < inputArray[y]:
                    valueIndex = y
        inputArray[x], inputArray[valueIndex] = inputArray[valueIndex], inputArray[x]
    return inputArray


# quick sort algorithm
def quickSort(inputArray, ascender = True):
    if len(inputArray) <= 1:
        return inputArray
    else:
        selection = inputArray.pop()
    greater = []
    lower = []
    for x in inputArray:
        if x > selection:
            greater.append(x)
        else:
            lower.append(x)
    if ascender:
        return quickSort(lower, ascender) + [selection] + quickSort(greater, ascender)
    else:
        return quickSort(greater, ascender) + [selection] + quickSort(lower, ascender)

        
##*****************************************************************************##

# FUNCTIONS TO DISPLAY BANNER
def banner():
    print(f"{colors['green']}{' '}{'_'*53}{' '}{colors['none']}")
    print(f"{colors['green']}|{colors['none']}{' '*2}{colors['blue']}Welcome to the Python Algorithm Sorting Programm{colors['none']}{' '*3}{colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']} {' '*51} {colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']} {' '*51} {colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{'-'*53}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']}{' '*5}{colors['blue']}Sorting Options{colors['none']}{' '*6}{colors['green']}|{' '*26}|{colors['none']}")
    print(f"{colors['green']}|{'_'*26}|{'_'*26}|{colors['none']}")
    print(f"{colors['green']}|{' '*26}|{' '*26}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']}{' '*5}{colors['yellow']}01 - Bubble Sort{colors['none']}{' '*5}{colors['green']}|{colors['none']}{' '*5}{colors['red']}When you provide{' '*5}{colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']}{' '*5}{colors['yellow']}02 - Section Sort{colors['none']}{' '*4}{colors['green']}|{colors['none']}{' '*5}{colors['red']}number for input,{' '*4}{colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{colors['none']}{' '*5}{colors['yellow']}03 - Quick Sort{colors['none']}{' '*6}{colors['green']}|{colors['none']}{' '*4}{colors['red']}Use , to seperate.{' '*4}{colors['green']}|{colors['none']}")
    print(f"{colors['green']}|{' '*26}|{' '*26}|{colors['none']}")
    print(f"{colors['green']}|{'_'*53}|{colors['none']}")
    print(" ")
    print(" ")

# FUNCTION TO CLEAR SCREEN 
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNCTION TO CHECK IF IS A NUMBER
def isNumber(input):
    try:
        int(input)
        return True
    except:
        return False

# FUNCTION TO CHECK IF IS ARRAY
def isNumberArray(input):
    try:
        for x in input.split(","):
            int(x)
        return True
    except:
        return False

# FUNCTION TO DISPLAY SORTED ARRAY 
def displayOutput(output):
    clearScreen()
    print(f"{colors['blue']}The sorted array is:{colors['none']}")
    print(f"{colors['green']}{output}{colors['none']}")
    print(" ")
    print(" ")
    input("Press any key to continue...")

## MAIN FUNCTION
def main():
    clearScreen()
    banner()
    # Get the sorting option
    print(f"{colors['yellow']}Please select the sorting option:{colors['none']}")
    sortingOption = input("Option: ")
    Time.sleep(1)
    if isNumber(sortingOption):
        sortingOption = int(sortingOption)
        clearScreen()
        banner()
        # Get the numbers to sort
        print(f"{colors['yellow']}Please enter the numbers to sort:{colors['none']}")
        inputArray = input("Numbers: ")
        Time.sleep(1)
        if isNumberArray(inputArray):
            inputArray = [int(x) for x in inputArray.split(",")]
            clearScreen()
            banner()
            if sortingOption == 1:
                print(f"IF you want to sort in ascending order press 1 else press 0")
                ascender = input("Option: ")
                if isNumber(ascender):
                    ascender = int(ascender)
                    if ascender == 1:
                        displayOutput(bubbleSort(inputArray, True))
                    elif ascender == 0:
                        displayOutput(bubbleSort(inputArray, False))
                    else:
                        print(f"{colors['red']}Please enter a valid number{colors['none']}")
                        Time.sleep(2)
                        main()
            elif sortingOption == 2:
                print(f"IF you want to sort in ascending order press 1 else press 0")
                ascender = input("Option: ")
                if isNumber(ascender):
                    ascender = int(ascender)
                    if ascender == 1:
                        displayOutput(selectionSort(inputArray, True))
                    elif ascender == 0:
                        displayOutput(selectionSort(inputArray, False))
                    else:
                        print(f"{colors['red']}Please enter a valid number{colors['none']}")
                        Time.sleep(2)
                        main()
            elif sortingOption == 3:
                print(f"IF you want to sort in ascending order press 1 else press 0")
                ascender = input("Option: ")
                if isNumber(ascender):
                    ascender = int(ascender)
                    if ascender == 1:
                        displayOutput(quickSort(inputArray, True))
                    elif ascender == 0:
                        displayOutput(quickSort(inputArray, False))
                    else:
                        print(f"{colors['red']}Please enter a valid number{colors['none']}")
                        Time.sleep(2)
                        main()
            else:
                print(f"{colors['red']}Please enter a valid number{colors['none']}")
                Time.sleep(2)
                main()

## RUN MAIN FUNCTION
main()



