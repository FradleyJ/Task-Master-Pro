# Task-Master-Pro
Task Master Pro is a Python-based To-Do List Application designed to help users manage their tasks effectively. With a focus on simplicity and functionality, it allows users to view, add, delete, and mark tasks as complete, all while keeping records persistently saved in a file. 
Features

View All Tasks: Display all tasks, including their descriptions, due dates, and statuses.

Add New Task: Easily add tasks with descriptions and due dates.

Delete Task: Remove tasks by their assigned numbers, with automatic renumbering for remaining tasks.

Mark Task as Complete: Update the status of a task to "Complete."

View Incomplete Tasks: Display only tasks that are still pending.

Persistent Storage: Tasks are saved to a file and loaded automatically at startup.

How to Use

Run the program in your Python environment.

Enter the file name where tasks will be stored or retrieved.

Choose an option from the menu:

1: View all tasks.

2: Add a new task.

3: Delete an existing task.

4: Mark a task as complete.

5: View incomplete tasks.

6: Exit the program.

Follow the prompts for each option.

Example Interaction

Welcome to Task Master Pro!

What is the file name? tasks.txt
Options:
1. View All Tasks
2. Add a New Task
3. Delete a Task
4. Mark a Task as Complete
5. View Incomplete Tasks
6. Exit
Choose an option: 1
No Tasks Found.

Choose an option: 2
What is the task you would like to add?
Buy groceries
When is the Due Date?
2024-12-31
Task added successfully.

Choose an option: 1
**Current Task**
1. Buy groceries - Due: 2024-12-31 - Status: Pending
**Current Task**

Choose an option: 4
What is the Task you would like to complete?
Use the number it starts with
1
Task marked as complete.

Choose an option: 5
No incomplete tasks found.
Good Work!

Choose an option: 6
Goodbye!

Requirements

Python 3.x

Error Handling

Invalid File Name: Notifies the user if the specified file is invalid or missing.

Empty Task List: Alerts the user when there are no tasks to display.

Invalid Input: Prompts the user to enter valid options or task numbers.

Author

Created by: Fradley Joseph

