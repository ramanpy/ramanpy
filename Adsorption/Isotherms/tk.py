from tkinter import*

def isotherm():
    print("You clicked to proceed ISOTHERM")

def submit():
    username = entry.get()
    print("Hello!"+username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


window=Tk()
window.geometry("600x400")
window.title("Adsorption")
icon=PhotoImage(file="Logo.png")
window.iconphoto(True,icon)
#photo=PhotoImage(file="Logo.png")
window.config(background="skyblue") #hex colour from google

'''label = Label(window,text="RamChemEdu",
              font=("Georgia",40,'bold'),
              fg='green',bg='orange',
              relief = RAISED, bd = 10,
              padx = 20,pady = 20,image=icon,compound='left').pack()'''
'''isotherm=Button(window,text='Isotherm',
                command = isotherm,
                font=('Arial',12),
                fg='green',bg='black').pack()'''
entry = Entry(window,font=("Arial",20))
entry.pack(side=LEFT)
subm = Button(window,text = "Submit",command = submit).pack(side=RIGHT)
delete = Button(window,text = "Delete",command = delete).pack(side=RIGHT)
backspace = Button(window,text = "Backspace",command = backspace).pack(side=RIGHT)


window.mainloop()