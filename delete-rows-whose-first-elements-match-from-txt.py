import os
def number_of_lines(folder_name):
    with open(folder_name, 'r') as folder:
        line_counts = sum(1 for satir in folder)
    return line_counts

def remove_line(folder_name, line_for_remove):

    with open(folder_name, 'r') as folder:
        clines = folder.readlines()

    if 0 <= line_for_remove <= len(clines):
        del clines[line_for_remove]  

        with open(folder_name, 'w') as folder:
            folder.writelines(clines)
        print(f"{line_for_remove}. line deleted.")
    else:
        print("The row in the specified row is not found in the folder.")

current_directory = os.getcwd()

file_path = os.path.realpath(__file__)
folder_path = os.path.dirname(file_path)

def main():

    folder_name = folder_path+"\\1.txt"
    numberforfirst = number_of_lines(folder_name)
    
    firsttxtline = folder_path+"\\1.txt"
    secondtxtline = folder_path+"\\2.txt"

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
   
    while numberforfirst > 0:

        firsttxt = firstlines[numberforfirst-1].strip().split(',')
        numberforsecond = number_of_lines("2.txt")
        
        while numberforsecond > 0:

            secondtxt = secondtxtlines[numberforsecond-1].strip().split(',')
            
            if str(firsttxt[0]) == str(secondtxt[0]):
                
                remove_line(folder_name, numberforfirst-1)

            numberforsecond = numberforsecond - 1

        numberforfirst = numberforfirst - 1

    print("process completed")


if __name__ == "__main__":
    main()
