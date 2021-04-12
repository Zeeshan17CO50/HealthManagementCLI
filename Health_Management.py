# Health Management System
# 3 Clients - Harry, Rohan, Hammad
# create 3 files to lock food and create another 3 files to lock her exercise- total 6 files
# write a function that when executed takes as input client_name
# [time] chicken, roti
# exercise: [] sheated solder press, cable crossover
# One more function to retrieve exercise or food for any client

import datetime
import os

if not os.path.exists('Details'):
    os.mkdir('Details')


def food_inserted():
    print("Food detail inserted successfully.")


def exer_inserted():
    print("Exercise detail inserted successfully.")


def get_date():
    return datetime.datetime.now()


def lock_harry_food(harry_food):
    with open('Details/harry_food.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {harry_food}\n")


def lock_rohan_food(rohan_food):
    with open('Details/rohan_food.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {rohan_food}\n")


def lock_hammad_food(hammad_food):
    with open('Details/hammad_food.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {hammad_food}\n")


def lock_harry_exercise(exercise):
    with open('Details/harry_exer.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {exercise}\n")


def lock_rohan_exercise(exercise):
    with open('Details/rohan_exer.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {exercise}\n")


def lock_hammad_exercise(exercise):
    with open('Details/hammad_exer.txt', 'a+') as f_h:
        f_h.write(f"[{get_date()}], {exercise}\n")


def retrieve_harry_food():
    with open('Details/harry_food.txt', 'r') as f_h:        # 'r'-read is by default
        for i in f_h:
            print(i, end="")


def retrieve_rohan_food():
    with open('Details/rohan_food.txt') as f_h:
        return f_h.readlines()


def retrieve_hammad_food():
    with open('Details/hammad_food.txt') as f_h:
        return f_h.readlines()


def retrieve_harry_exercise():
    with open('Details/harry_exer.txt', 'r') as f_h:
        return f_h.readlines()


def retrieve_rohan_exercise():
    with open('Details/rohan_exer.txt', 'r') as f_h:
        return f_h.readlines()


def retrieve_hammad_exercise():
    with open('Details/hammad_exer.txt', 'r') as f_h:
        return f_h.readlines()


while True:
    print("\n", "-"*10, "Menu", "-"*10)
    ch = int(input("1. Lock.\n2. Retrieve.\n3. Exit.\nEnter a choice: "))
    if ch == 1:
        print("\n", "-"*10, "Lock", "-"*10)
        ch1 = int(input("1. Food\n2. Exercise\nEnter a choice: "))
        if ch1 == 1:
            print("\n", "-"*10, "Food", "-"*10)
            ch2 = int(input("1. Harry\n2. Rohan\n3. Hammad\nEnter a choice: "))
            if ch2 == 1:
                harry_food = input("Enter food u eat: ")
                lock_harry_food(harry_food)
                food_inserted()
                continue
            elif ch2 == 2:
                rohan_food = input("Enter food u eat: ")
                lock_rohan_food(rohan_food)
                food_inserted()
                continue
            elif ch2 == 3:
                hammad_food = input("Enter food u eat: ")
                lock_hammad_food(hammad_food)
                food_inserted()
                continue
            else:
                print("Enter valid input.")
                continue

        elif ch1 == 2:
            print("\n", "-"*10, "Exercise", "-"*10)
            ch2 = int(input("1. Harry\n2. Rohan\n3. Hammad\nEnter a choice: "))
            if ch2 == 1:
                harry_exer = input("Enter exercise u do: ")
                lock_harry_exercise(harry_exer)
                exer_inserted()
                continue
            elif ch2 == 2:
                rohan_exer = input("Enter exercise u do: ")
                lock_rohan_exercise(rohan_exer)
                exer_inserted()
                continue
            elif ch2 == 3:
                hammad_exer = input("Enter exercise u do: ")
                lock_hammad_exercise(hammad_exer)
                exer_inserted()
                continue
            else:
                print("Enter valid input.")
                continue
        else:
            print("Enter valid input.")
            continue

    if ch == 2:
        print("\n", "-"*10, "Retrieve", "-"*10)
        ch1 = int(input("1. Food\n2. Exercise\nEnter a choice: "))
        if ch1 == 1:
            print("\n", "-"*10, "Food", "-"*10)
            ch2 = int(input("1. Harry\n2. Rohan\n3. Hammad\nEnter a choice: "))
            if ch2 == 1:
                retrieve_harry_food()
                continue
            elif ch2 == 2:
                print(retrieve_rohan_food())
                continue
            elif ch2 == 3:
                print(retrieve_hammad_food())
                continue
            else:
                print("Enter valid input.")
                continue

        elif ch1 == 2:
            print("\n", "-"*10, "Exercise", "-"*10)
            ch2 = int(input("1. Harry\n2. Rohan\n3. Hammad\nEnter a choice: "))
            if ch2 == 1:
                print(retrieve_harry_exercise())
                continue
            elif ch2 == 2:
                print(retrieve_rohan_exercise())
                continue
            elif ch2 == 3:
                print(retrieve_hammad_exercise())
                continue
            else:
                print("Enter valid input.")
                continue
        else:
            print("Enter valid input.")
            continue

    elif ch == 3:
        print("Bye.")
        break

    else:
        print("Please enter correct choice.")


'''
client_list = {1:"Harry", 2:"Rohan", 3:"Hammad"}
log_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value,"\n", end="")
    client_name = int(input())
        
    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value,"\n", end="")
        log_name =  int(input())
        print("Selected Job : ", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()).replace(":","-") + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        log_name =  int(input())
        print(client_list[client_name], "-", log_list[log_name], "Report :","\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close() 
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")
'''