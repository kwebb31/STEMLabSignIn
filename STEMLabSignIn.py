import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#overwrites the previous information in the file to create a newly emptied file, writes, and closes the file. 
oldfile = open("studentInfo.txt", "w")
oldfile.write("")
oldfile.close()

#the rest of the writes will be appends so they don't get overwritten
outfile = open("studentInfo.txt", "a")
class StudentGUI:
    def __init__(self, master=None):
        self.root = master
        if self.root is None:
            self.root = tk.Tk()
            self.root.title("Student Menu")
            self.root.geometry("800x600")  # Set initial window size

        self.create_widgets()

    def create_widgets(self):
        #the frame that is created, the color and the way that the frame is used 
        self.frame = tk.Frame(self.root, bg="#333333")
        self.frame.pack(expand=True, fill="both")
        
        #the label for the window
        self.label = ttk.Label(self.frame, text="Enter Student ID:", font=("Helvetica", 18), background="#333333", foreground="white")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        #formatting the text and patterns of the entries
        self.entry = ttk.Entry(self.frame, font=("Helvetica", 18))
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        #Doubling width of the buttons
        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.submit_id, width=40)
        self.submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def submit_id(self):
        #gets the entry for the student id and removes any whitespace or extrraneous chracters
        student_id = self.entry.get().strip()
       
        #ensures that the netID is not empty
        if student_id == "":
            self.show_error("Please enter a student ID.")
        #Checks to make sure that the first and second chars are alphabetical, and that the last four are numbers.
        elif student_id[0].isalpha() == False or  student_id[1].isalpha() == False or student_id[2].isnumeric() == False or student_id[3].isnumeric() == False or student_id[4].isnumeric == False or student_id[5].isnumeric() == False:
            self.show_error("Please enter a valid student ID.")
        #the break statement so that LAs can end the day and close the program
        elif student_id.lower() in ["exit", "stop"]:
            print("Thanks for your hard work today!")
            self.show_LA("Thanks for your hard work!")
            self.root.destroy()
        else:
            # Writing student information to file
            with open("studentInfo.txt", "a") as outfile:
                outfile.write(f"{student_id}, ")
                # Get current date
                current_date = datetime.now()
                formatted_date = current_date.strftime("%m/%d/%y")
                outfile.write(f"{formatted_date}, ")

            self.create_course_menu()

    def create_course_menu(self):
        # Create new window for course selection
        course_window = tk.Toplevel(self.root)
        course_window.title("Course Selection")
        course_window.geometry("400x300")

        #background and frame for the course page
        course_frame = tk.Frame(course_window, bg="#333333")
        course_frame.pack(expand=True, fill="both")

        course_label = ttk.Label(course_frame, text=f"Welcome Student ID: {self.entry.get()}", font=("Helvetica", 18), background="#333333", foreground="white")
        course_label.pack(padx=10, pady=10)

        # Doubling width of the buttons
        course_button = ttk.Button(course_frame, text="Course", command=self.select_course, width=40)
        course_button.pack(padx=10, pady=10)

        general_study_button = ttk.Button(course_frame, text="General Study", command=self.general_study, width=40)
        general_study_button.pack(padx=10, pady=10)

    def select_course(self):
        print("Course selected")
        # Add your course selection logic here
        with open("studentInfo.txt", "a") as outfile:
            choice = "course\n"
            outfile.write(choice)

        self.root.destroy()  # Close previous window
        StudentGUI()  # Open new window for next entry

    def general_study(self):
        print("General Study selected")
        # Add your general study logic here
        with open("studentInfo.txt", "a") as outfile:
            choice = "general\n"
            outfile.write(choice)

        self.root.destroy()  # Close previous window
        StudentGUI()  # Open new window for next entry

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_LA(self, message):
        messagebox.showinfo(title="Have a good day", message="Thank you for your hard work!")


def main():
    app = StudentGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main()
