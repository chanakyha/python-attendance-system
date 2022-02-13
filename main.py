from prettytable import PrettyTable
from termcolor import colored
import os
#chan san

def clrscr():
    os.system("cls") | os.system("clear")


# Clearing the screen brfore starting
clrscr()

print(colored("WELCOME TO SCHOOL ATTENDANCE SYSTEM", "white", "on_red"))
mainTable = PrettyTable(["Enter", "Choice"])
mainTable.add_row(["Teacher's Login", "1"])
mainTable.add_row(["Student's Login", "2"])
mainTable.add_row(["Create Account", "3"])
print(mainTable)

choice = None

while (not choice):
    choice = input("Enter the choice: ")
