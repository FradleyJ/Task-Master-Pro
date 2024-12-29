# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:00:05 2024

@author: Fradley Joseph
"""

print("Welcome to the To-Do List Application!\n")
#option = input(("Options:\n1. View All Tasks\n2. Add a New Task\n3. Mark a Task as Complete\n4. Delete a Task\n5. View Incomplete Tasks\n6. Exit\nChoose an option: "))
import os
import sys

def view_all_tasks(file):
    try:
        with open(file, 'r') as document:
            if os.stat(file).st_size == 0:
                print('No Tasks Found.')
            else:
                print("**Current Task**")
                for task in document:
                    print(task.strip())
                print("**Current Task**")
    except:
        print("Error 410:\nInvalid File Name!\nCreate A Text File in same Directory 1st.")
#task_name = input("What is the file name?\n")
#view_all_tasks(task_name)

def add_task(file, task_to_add, due_date):
    try:
        if os.stat(file).st_size == 0:
            storage = '1. ' + task_to_add + ' - Due: ' + due_date + ' - Status: Pending'
        else:
            count = 1
            with open(file, 'r') as document:
                for line in document:
                    count += 1      
            storage =   '\n' + str(count) + '. ' + task_to_add + ' - Due: ' + due_date + ' - Status: Pending'
        with open(file, 'a') as document:
            document.write(storage)
            print("Task added successfully.")
    except:
        print("Error! Try Again")
        
#add_task("AddTaskTest.txt", "New Task", "2024-28-12")

def complete_task(file, task_num_to_complete):
    with open(file, 'r') as document:
        lines = document.readlines()
                #for line in document:   
    with open(file, 'w') as document2:
        for line in lines:
            if line[0] == str(task_num_to_complete):
                finder = line.find('Status') + 7
                storage = line[:finder]
                final = storage + ' Complete' + '\n'
                document2.write(final)
            else:
                document2.write(line)
#complete_task('AddTaskTest.txt', 4)

def delete_task(file, task_to_delete):
    with open(file, 'r') as document:
        lines = document.readlines()
    with open(file, 'w') as document2:
        for line in lines:
            finder2 = line.find('.')
            if line[:finder2] == str(task_to_delete):
                continue
            else:
                document2.write(line)
    with open(file, 'r') as document3:
        line_3 = document3.readlines()
        
    with open(file, 'w') as document4:
        counter = 0
        for line in line_3:
            counter += 1
            finder = line.find('.')
            storage = line[finder:]
            final = str(counter) + storage
            document4.write(final)
#delete_task('AddTaskTest.txt',2)

def incomplete_task(file):
    with open(file, 'r') as document:
        lines = document.readlines()
        count = 0
        for line in lines:
            finder = line.find('Status:') + 7
            if 'Status: Pending' in line:
                print(line.strip())
                count += 1
            else:
                continue
        if count == 0:
            print("No incomplete tasks found.\nGood Work!")
#incomplete_task('AddTaskTest.txt')


def choose_option(option, file):
    if option == '1':
        #file = input("What is the file name?\n")
        view_all_tasks(file)
    elif option == '2':
        #file = input("What is the file name?\n")
        task_to_add = input("What is the task you would like to add?\n")
        due_date = input("When is the Due Date?\nExample Format: MM-DD-YYYY")
        add_task(file, task_to_add, due_date)
    elif option == '3':
        #file = input("What is the file name?\n")
        task_to_delete = input('What is the Task you would like to delete?\nUse the number it starts with\n')
        delete_task(file, task_to_delete)
    elif option == '4':
        #file = input("What is the file name?\n")
        task_num_to_complete = int(input('What is the Task you would like to complete?\nUse the number it starts with\n'))
        complete_task(file, task_num_to_complete)
    elif option == '5':
        #file = input('What is the file name?\n')
        incomplete_task(file)
    elif option == '6':
        print("Goodbye!")
        sys.exit()
    else:
        sys.exit()

file = input("What is the file name?")
while True:
    option = input(("Options:\n1. View All Tasks\n2. Add a New Task\n3. Delete a Task\n4. Mark a Task as Complete\n5. View Incomplete Tasks\n6. Exit\nChoose an option: "))   
    choose_option(option, file)
