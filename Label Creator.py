import csv
from tkinter import *

myGui = Tk()
myGui.title("Label Creator    v: 3.0")
myGui.geometry("290x70")

allArray = []
oddArray = []
evenArray = []

Label(myGui, text="Starting value: ").grid(row=0)
Label(myGui, text="Ending value: ").grid(row=1)

a = IntVar()
b = IntVar()

e1 = Entry(myGui, textvariable=a)
e1.grid(row=0, column=1)
e2 = Entry(myGui, textvariable=b)
e2.grid(row=1, column=1)

def main():
    oute1 = a.get()
    oute2 = b.get()
    for i in range(oute1, oute2 + 1):
        x = i
        allArray.append(x)
        # Odds
        if(x % 2 == 1):
            oddArray.append(x)
        # Evens
        elif(x % 2 == 0):
            evenArray.append(x)

    with open("all_labels", "w") as outputFile:
        writer1 = csv.writer(outputFile, lineterminator='\n')
        for item in allArray:
            writer1.writerow([item,''])


    with open("odd_labels", "w") as outputFile1:
        writer2 = csv.writer(outputFile1, lineterminator='\n')
        for item in oddArray:
            writer2.writerow([item,''])

    with open("even_labels", "w") as outputFile2:
        writer3 = csv.writer(outputFile2, lineterminator='\n')
        for item in evenArray:
            writer3.writerow([item,''])


Button(myGui, text="Start", command=main).grid(row=3)

myGui.mainloop()