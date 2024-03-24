# STEMLabSignIn
Sign in application for the CSUEB STEM Lab. Requests a student ID and then asks if a student is there for course or general study. Saves the student ID, current date, and course/general study to a text file with CSVs. 

This is a simple Python application built using Tkinter for creating an interactive student ID entry system. The application allows users to input their student ID or use the keywords "exit" or "stop" to exit the program.

## Features:
* Input student ID: Users can input their student ID into the application.
![image](https://github.com/kwebb31/STEMLabSignIn/assets/121592902/208e8e20-615a-410d-a016-d8c2e93a2717)

* Exit option: Users can type "exit" or "stop" to exit the application.
  ![image](https://github.com/kwebb31/STEMLabSignIn/assets/121592902/29bb0bde-1ffa-42e8-83d3-35fb853e950e)

* Course selection: After entering a student ID, users can select between taking a course or general study.
![image](https://github.com/kwebb31/STEMLabSignIn/assets/121592902/fc564f90-9d61-467d-aa22-590508c1f4d7)

* File Storage: The netID of the student, the current date, and course or general study will be stored in the studentInfo.txt file as CSVs. It will update daily (all information from the previous day will be cleared). To change this, delete the following two lines of code in your source Python file: 

![image](https://github.com/kwebb31/STEMLabSignIn/assets/121592902/524ed8d5-0d25-452f-bea5-94f7c6044445)

## Usage:
* Launch the application.
* Enter your student ID in the provided input field.
* Click the "Submit" button to proceed.
* Choose between taking a course or general study.
* Repeat steps 2-4 for additional entries.


## Requirements:
Python 3.x
Tkinter library
Installation:
No installation required. Simply download or clone the repository and run the Python script.

## Usage Example:
python STEMLabSignIn.py
