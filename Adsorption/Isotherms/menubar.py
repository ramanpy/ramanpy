from tkinter import*


def openFile():
    print("You opened a File!")
def saveFile():
    print("You saved a File!")

def cutFile():
    print("You Cut a File!")
def copyFile():
    print("You Copy a File!")
def pasteFile():
    print("You Paste a File!")


window=Tk()

menubar = Menu(window)
window.config(menu = menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command = openFile)
fileMenu.add_command(label='Save',command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command = quit)



editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'Edit',menu=editMenu)
editMenu.add_command(label = 'Cut',command = cutFile)
editMenu.add_command(label = 'Copy',command = copyFile)
editMenu.add_command(label = 'Paste',command = pasteFile)
window.mainloop()