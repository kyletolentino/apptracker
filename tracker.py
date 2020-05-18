from tkinter import *

# creates a window object
app = Tk()

# company
company_text = StringVar()
company_label = Label(app, text='Company', font=('bold', 14), pady=20)
company_label.grid(row=0, column=0, sticky=W)
company_entry = Entry(app, textvariable=company_text)
company_entry.grid(row=1, column=0)

# job id
id_text = StringVar()
id_label = Label(app, text='Job ID', font=('bold', 14), pady=20)
id_label.grid(row=0, column=1, sticky=W)
id_entry = Entry(app, textvariable=id_text)
id_entry.grid(row=1, column=1)

app.title('Application Tracker')
app.geometry('800x400')

# run program
app.mainloop()