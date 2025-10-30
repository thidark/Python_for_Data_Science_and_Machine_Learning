#Opening and Closing Files
#Reading and Writing Files
#Appending to Files

#Open a file in write mode
file = open("sample.txt", "w") 
#Write some text to the file
file.write("Hello, World!\n") 

with open("sample.txt", "r") as file:
    cotent=file.read()
    print(cotent)
    
#Close the file
file.close()

#-------------------------------------
#file handling : CSV files
import csv
def read_csv(filename):
    data = []
    with open(filename, mode='r', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row)
    return data
print(read_csv('users.csv'))