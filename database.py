from tkinter import *
import csv
from tkinter import messagebox as ms
import uuid

# Setting this as global so it can be accessed and be manipulated all throughout the body
global data
global row
data = []
with open('saver.txt', 'r') as rf:
    n = csv.reader(rf)
    for row in n:
        if row:
            data.append(row)


# Main Class which consist of all operations and codes for the GUI
class main:
    def __init__(self, master):
        self.master = master
        self.fullname = StringVar()
        self.yrlvl = StringVar()
        self.course = StringVar()
        self.idnumber = StringVar()
        self.var = StringVar()


        self.n_fullName = StringVar()
        self.n_yrlvl = StringVar()
        self.n_course = StringVar()
        self.n_number = StringVar()
        self.n_var = StringVar()
        self.n_idNumber = StringVar()
        # Create Widgets
        self.widgets()

    # This Function is used to search and verify if a contact exists
    def search_students(self):
        mirror = bool
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if field == idnumber:
                    mirror = True
                    print(row)
                    

                    # fullname
                    Label(self.find, text='Full Name: ', font=('', 15), pady=5, padx=5).grid(row=4, column=0)
                    name = Label(self.find, text=str(row[0]), font=('', 15))
                    name.grid(row=4, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateName).grid(row=4,
                                                                                                              column=2)
                    # Year Level
                    Label(self.find, text='Year Level: ', font=('', 15), pady=5, padx=5).grid(row=5, column=0)
                    yrlvl = Label(self.find, text=row[1], font=('', 15))
                    yrlvl.grid(row=5, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateYearlvl).grid(row=5,
                                                                                                                column=2)
                    # course
                    Label(self.find, text='Course: ', font=('', 15), pady=5, padx=5).grid(row=6, column=0)
                    course = Label(self.find, text=row[2], font=('', 15))
                    course.grid(row=6, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateCourse).grid(row=6,
                                                                                                              column=2)

                    # ID Number
                    Label(self.find, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(row=7, column=0)
                    idno = Label(self.find, text=row[3], font=('', 15))
                    idno.grid(row=7, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateIdNumber).grid(row=7,
                                                                                                                column=2)

                    Button(self.find, text='UPDATE', bd=3, font=('', 15), padx=5, command=self.update_writer).grid(row=10,
                                                                                                                 column=0)
                    Button(self.find, text='DELETE', bd=3, font=('', 15), padx=5, command=self.Delete).grid(row=10,
                                                                                                            column=1)
                    
        if mirror != True:
            ms.showerror('Error!', 'ID Number does not exist!')

    # This Function is used Edit the Name of the student
    def UpdateName(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if field == idnumber:
                    Entry(self.find, textvariable=self.n_fullName, bd=5, font=('', 15)).grid(row=4, column=1)
                    x = int()
                    idnumber = self.n_idNumber.get()
                    full_name = self.n_fullName.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == idnumber:
                                    row[0] = full_name
                                    x = 1
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)


    def UpdateYearlvl(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if field == idnumber:
                    Entry(self.find, textvariable=self.n_yrlvl, bd=5, font=('', 15)).grid(row=5, column=1)
                    x = int()
                    idnumber = self.n_idNumber.get()
                    year_lvl = self.n_yrlvl.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == idnumber:
                                    row[1] = year_lvl
                                    x = 1
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)



    # This Function is used Edit the email of the student
    def UpdateCourse(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if field == idnumber:
                    Entry(self.find, textvariable=self.n_course, bd=5, font=('', 15)).grid(row=6, column=1)
                    x = int()
                    idnumber = self.n_idNumber.get()
                    course_info = self.n_course.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == idnumber:
                                    row[2] = course_info
                                    x = 1
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    def UpdateIdNumber(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if field == idnumber:
                    Entry(self.find, textvariable=self.n_idNumber, bd=5, font=('', 15)).grid(row=7, column=1)
                    x = int()
                    mirror = bool
                    id_number = self.n_idNumber.get()
                    for row in data:
                        for field in row:
                            if field == self.idnumber.get():
                                mirror = True
                    if mirror == True:
                        ms.showerror('Oops!', 'A student with the same ID number already exists')
                    else:
                     while x != 1:
                        for row in data:
                            for field in row:
                                if field == idnumber:
                                    row[3] = id_number
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    def update_writer(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if idnumber == field:
                    data.append(self.fullname)
                    data.append(self.yrlvl)
                    data.append(self.course)
                    data.append(self.idnumber)
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)

                    for line in data:
                        write_data.writerow(line)
                        
        ms.showinfo('Success!', 'Student Info Updated')
        with open('saver.txt', 'w') as wf:
            write_data = csv.writer(wf)
            for line in data:
                write_data.writerow(line)
        root.destroy()

    def Delete(self):
        idnumber = self.n_idNumber.get()
        for row in data:
            for field in row:
                if idnumber == field:
                    data.remove(row)
                    with open('saver.txt', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)
        ms.showinfo('Success!', 'Student Info Deleted')
        with open('saver.txt', 'w') as wf:
            write_data = csv.writer(wf)
            for line in data:
                write_data.writerow(line)
        root.destroy()

    def add_student(self):
        id_number = str()
        yrlvl = self.yrlvl.get()
        mirror = bool
        fullname = self.fullname.get()
        idnumber = self.idnumber.get()
        for row in data:
            for field in row:
                if field == self.fullname.get():
                    mirror = True
        if mirror == True:
            ms.showerror('Oops!', 'A student with the same name already exists')
        else:
            course = self.course.get()
            type = self.var.get()
            id = uuid.uuid4()
            #print(type)
            
            with open('saver.txt', 'a') as rf:
                fieldnames = ['FULL_NAME', 'YEAR_LEVEL', 'COURSE', 'ID_NUMBER']
                n = csv.DictWriter(rf, fieldnames=fieldnames)
                n.writerow(
                    {'FULL_NAME': fullname,'YEAR_LEVEL': yrlvl, 'COURSE': course, 'ID_NUMBER': idnumber, })
                
            ms.showinfo('Success!', 'Student Info Added')
            root.destroy()

    # This Functions are used to setup the Packing methods of the widgets for the GUI
    def main(self):
        self.n_fullName.set('')
        self.n_course.set('')
        self.create.pack_forget()
        self.head['text'] = 'Select Your Choice'
        self.home.pack()

    def add(self):
        self.n_fullName.set('')
        self.n_course.set('')
        self.home.pack_forget()
        self.head['text'] = 'Add New Student'
        self.create.pack()

    def search(self):
        self.n_fullName.set('')
        self.n_course.set('')
        self.home.pack_forget()
        self.create.pack_forget()
        self.find.pack_forget()
        self.head['text'] = 'Search Student'
        self.find.pack()

    # This is used to setup the interface
    def widgets(self):
        # entry part
        self.head = Label(self.master, text="Select Your Choice", font=('', 20))
        self.head.pack()
        Label(self.master, text="").pack()

        ##------- HOME --------##
        self.home = Frame(self.master, padx=10, pady=1, )
        # buttons part
        Button(self.home, text=' Search Student ', bd=3, font=('', 12), padx=5, pady=5, command=self.search).pack()
        Label(self.home, text="").pack()
        Button(self.home, text='   Add Student  ', bd=3, font=('', 12), padx=5, pady=5, command=self.add).pack()
        Label(self.home, text="").pack()
        self.home.pack()

        ##------- ADD Students --------##
        self.create = Frame(self.master, padx=10, pady=10)
        Label(self.create, text='Full Name: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=2, column=0)
        Entry(self.create, textvariable=self.fullname, bd=5, font=('', 15)).grid(row=2, column=1)


        Label(self.create, text='Year Level: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.yrlvl, bd=5, font=('', 15)).grid(row=3, column=1)

        Label(self.create, text='Course: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.course, bd=5, font=('', 15)).grid(row=4, column=1)

        Label(self.create, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.idnumber, bd=5, font=('', 15)).grid(row=5, column=1)

        Label(self.create, text='').grid(sticky=W)

        Button(self.create, text='Add Student', bd=3, font=('', 15), padx=5, pady=5, command=self.add_student).grid(
            row=8, columnspan=4)
        
        ##------- SEARCH --------##
        self.find = Frame(self.master, padx=10, pady=10)
        Label(self.find, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=2, column=0)
        Entry(self.find, textvariable=self.n_idNumber, bd=5, font=('', 15)).grid(row=2, column=1)
        Button(self.find, text='Search', bd=3, font=('', 15), padx=5, pady=5, command=self.search_students).grid(
                                                                                                            column=1)



# Runs the GUI
root = Tk()
main(root)
root.title("Students")
root.mainloop()