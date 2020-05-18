from tkinter import *

# creates a window object
app = Tk()

# company
company_text = StringVar()
company_label = Label(app, text='Company', font=('bold', 14), pady=20)
company_label.grid(row=0, column=0, sticky=W)
company_entry = Entry(app, textvariable=company_text)
company_entry.grid(row=0, column=1)

# job id
id_text = StringVar()
id_label = Label(app, text='Job ID', font=('bold', 14), pady=20)
id_label.grid(row=0, column=2, sticky=W)
id_entry = Entry(app, textvariable=id_text)
id_entry.grid(row=0, column=3)

# box to show all applications
jobs_list = Listbox(app, height=17, width=90, border=0)
jobs_list.grid(row=2, column=0, columnspan=8, rowspan=8, pady=20, padx=20)

# scrollbar and conncet to box
scroll = Scrollbar(app)
scroll.grid(row=2, column=8)
jobs_list.configure(yscrollcommand=scroll.set)
# basically saying scroll along the y axis
scroll.configure(command=jobs_list.yview)

app.title('Application Tracker')
app.geometry('800x400')

# run program
app.mainloop()