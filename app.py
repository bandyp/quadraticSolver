from database import create_table, add_entry, get_entries
import math

menu = """ Please select one of the following options:
1) Add new coordinates
2) View entries
3) Exit

Your selection: """ 
welcome = "Welcome to the solution!"

def prompt_new_entry():
    entry_x_coordinates = input("What are the x coordinates? ")
    entry_y_coordinates = input("What are the y coordinates? ")

    add_entry(entry_x_coordinates, entry_y_coordinates)

def view_entries(entries):
    for entry in entries:
        print(f"{entry[0]}\n{entry[1]}\n\n")

print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print ("Invalid")
