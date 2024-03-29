import os
import time

def number_of_lines(folder_name):
    with open(folder_name, 'r') as folder:
        line_counts = sum(1 for satir in folder)
    return line_counts

def remove_line(folder_name, line_for_remove):
    with open(folder_name, 'r') as folder:
        clines = folder.readlines()

    if 0 < line_for_remove <= len(clines):
        del clines[line_for_remove - 1]

        with open(folder_name, 'w') as folder:
            folder.writelines(clines)
        print(f"{line_for_remove}. line deleted.")
    else:
        print("The specified row is not found in the folder or invalid row number.")




def main():

    file_path = os.path.realpath(__file__)
    folder_path = os.path.dirname(file_path)
    
    
    folder_name = "C:\\python-tests\\1.txt"
    numberforfirst = number_of_lines(folder_name)
    
    
    firsttxtline = "C:\\python-tests\\1.txt"
    secondtxtline = "C:\\python-tests\\2.txt"

    with open(firsttxtline, "r") as folder:
        firstlines = folder.readlines()

    if not firstlines:
        print("folder format is not suitable. The loop is terminating.")
        return 
    
    with open(secondtxtline, "r") as folder:
        secondtxtlines = folder.readlines()

    if not secondtxtlines:
        print("folder format is not suitable. The loop is terminating.")
        return
    print(numberforfirst)
    
    while numberforfirst > 0:

        firsttxt = firstlines[numberforfirst-1].strip().split(',')
        numberforsecond = number_of_lines(secondtxtline)
        print(numberforsecond)
        
        while numberforsecond >= 0:

            secondtxt = secondtxtlines[numberforsecond-1].strip().split(',')
            
            if (firsttxt[0]) == (secondtxt[0]):
                remove_line(folder_name, numberforfirst)
                numberforsecond = 0
            else:

                numberforsecond = numberforsecond - 1


        numberforfirst = numberforfirst - 1

    print("process completed")


if __name__ == "__main__":
    main()
