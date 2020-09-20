from tkinter import *
from  tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import tkinter.messagebox as tmsg
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global  file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
#             save as new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Untitled")
    else:
#         save file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("About","This is notepad by Pratibha")

if __name__=='__main__':
    root=Tk()
    root.geometry("700x700")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("1.icon.png")

    TextArea=Text(root,font="Lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    # menubar
    menubar=Menu(root)
    m1=Menu(menubar,tearoff=0)
    m1.add_command(label="New",command=newFile)
    m1.add_command(label="Open",command=openFile)
    m1.add_command(label="Save", command=saveFile)
    m1.add_separator()
    m1.add_command(label="Exit", command=quitApp)
    root.config(menu=menubar)
    menubar.add_cascade(label="File",menu=m1)

    m2=Menu(menubar,tearoff=0)
    m2.add_command(label="Cut", command=cut)
    m2.add_command(label="Copy", command=copy)
    m2.add_command(label="Paste", command=paste)
    root.config(menu=menubar)
    menubar.add_cascade(label="Edit",menu=m2)

    m3=Menu(menubar,tearoff=0)
    m3.add_command(label="About", command=about)
    root.config(menu=menubar)
    menubar.add_cascade(label="Help",menu=m3)

#     scrollbar
    scroll=Scrollbar(TextArea)
    scroll.pack(fill=Y,side=RIGHT)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)

    root.mainloop()
