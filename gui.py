from tkinter import *
from tkinter.messagebox import *

import fileManagerExtension as fex
import fileManagerName as fna

class MyGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("630x320+250+100")
        self.main_window.title("File Manager")
        
        # Frames
        self.frame1 = Frame(self.main_window, width=630, height=160, bg="#2f3f73")
        self.frame1.place(x=0, y=0)
        self.frame2 = Frame(self.main_window, width=630, height=160, bg="#09133b")
        self.frame2.place(x=0, y=160)
        
        #-----------------------------------------Frame1-----------------------------------------
        
        # Title
        self.moveLabelE = Label(self.frame1, text="Move Files by Extension", font=("Arial", 20), bg="#2f3f73", fg="white")
        self.moveLabelE.place(x=20, y=0)
        
        
        # Paths
        self.fromPathLabelE = Label(self.frame1, text="From", font=14, bg="#2f3f73", fg="white")
        self.fromPathLabelE.place(x=20, y=40)
        self.fromPathEntryE = Entry(self.frame1, width=35, font=14, bg="#09133b", fg="white")
        self.fromPathEntryE.place(x=60, y=40)

        self.toPathLabelE = Label(self.frame1, text="To", font=14, bg="#2f3f73", fg="white")
        self.toPathLabelE.place(x=20, y=70)
        self.toPathEntryE = Entry(self.frame1, width=35, font=14, bg="#09133b", fg="white")
        self.toPathEntryE.place(x=60, y=70)
        
        
        # file extension
        self.typeLabelE = Label(self.frame1, text="File Extension", font=14, bg="#2f3f73", fg="white")
        self.typeLabelE.place(x=410, y=40)
        self.typeEntryE = Entry(self.frame1, width=10, font=14, bg="#09133b", fg="white")
        self.typeEntryE.place(x=500, y=40)
        
        
        # Rename
        self.renameLabelE = Label(self.frame1, text="Rename(optional)", font=14, bg="#2f3f73", fg="white")
        self.renameLabelE.place(x=20, y=120)
        self.renameEntryE = Entry(self.frame1, width=10, font=14, bg="#09133b", fg="white")
        self.renameEntryE.place(x=130, y=120)
        
        
        # buttons
        self.moveFileBtnE = Button(self.frame1, text="Move", font=14, command=self.moveFilesE, bg="#09133b")
        self.moveFileBtnE.place(x=530, y=90)
        self.copyFileBtnE = Button(self.frame1, text="Copy", font=14, command=self.copyFilesE, bg="#09133b")
        self.copyFileBtnE.place(x=530, y=120)
        #self.zipFileBtn = Button(self.frame1, text="Zip", font=14, command=self.zipFilesE, bg="#09133b")
        #self.zipFileBtn.place(x=470, y=120)

        
        self.fileOrderE=StringVar()
        self.fileOrderE.set("asc")
        self.ascOrderE=Radiobutton(self.frame1, text="Ascending", font=14, variable=self.fileOrderE, value="asc", bg="#2f3f73", fg="white")
        self.ascOrderE.place(x=235, y=120)
        self.desOrderE=Radiobutton(self.frame1, text="Descending", font=14, variable=self.fileOrderE, value="desc", bg="#2f3f73", fg="white")
        self.desOrderE.place(x=335, y=120)
        
        #-----------------------------------------Frame1-----------------------------------------
        
        #-----------------------------------------Frame2-----------------------------------------
        
        # Title
        self.moveLabelN = Label(self.frame2, text="Move Files by Name", font=("Arial", 20), bg="#09133b", fg="white")
        self.moveLabelN.place(x=20, y=0)
        
        
        # Paths
        self.fromPathLabelN = Label(self.frame2, text="From", font=14, bg="#09133b", fg="white")
        self.fromPathLabelN.place(x=20, y=40)
        self.fromPathEntryN = Entry(self.frame2, width=35, font=14, bg="#2f3f73", fg="white")
        self.fromPathEntryN.place(x=60, y=40)

        self.toPathLabelN = Label(self.frame2, text="To", font=14, bg="#09133b", fg="white")
        self.toPathLabelN.place(x=20, y=70)
        self.toPathEntryN = Entry(self.frame2, width=35, font=14, bg="#2f3f73", fg="white")
        self.toPathEntryN.place(x=60, y=70)
        
        
        # file name
        self.nameLabelN = Label(self.frame2, text="File Name", font=14, bg="#09133b", fg="white")
        self.nameLabelN.place(x=435, y=40)
        self.nameEntryN = Entry(self.frame2, width=10, font=14, bg="#2f3f73", fg="white")
        self.nameEntryN.place(x=500, y=40)
        
        
        # Rename
        self.renameLabelN = Label(self.frame2, text="Rename(optional)", font=14, bg="#09133b", fg="white")
        self.renameLabelN.place(x=20, y=120)
        self.renameEntryN = Entry(self.frame2, width=10, font=14, bg="#2f3f73", fg="white")
        self.renameEntryN.place(x=130, y=120)
        
        
        # buttons
        self.moveFileBtnN = Button(self.frame2, text="Move", font=14, command=self.moveFilesN, bg="#2f3f73")
        self.moveFileBtnN.place(x=530, y=90)
        self.copyFileBtnN = Button(self.frame2, text="Copy", font=14, command=self.copyFilesN, bg="#2f3f73")
        self.copyFileBtnN.place(x=530, y=120)
        #self.zipFileBtn = Button(self.frame2, text="Zip", font=14, command=self.zipFilesN, bg="#2f3f73")
        #self.zipFileBtn.place(x=470, y=120)

        
        self.fileOrderN=StringVar()
        self.fileOrderN.set("asc")
        self.ascOrderN=Radiobutton(self.frame2, text="Ascending", font=14, variable=self.fileOrderN, value="asc", bg="#09133b", fg="white")
        self.ascOrderN.place(x=235, y=120)
        self.desOrderN=Radiobutton(self.frame2, text="Descending", font=14, variable=self.fileOrderN, value="desc", bg="#09133b", fg="white")
        self.desOrderN.place(x=335, y=120)
        
        #-----------------------------------------Frame2-----------------------------------------
        
        mainloop()
    
            
    def moveFilesE(self):
        fex.processFiles("move", self.fromPathEntryE.get(), self.toPathEntryE.get(),
                           "." + self.typeEntryE.get(), self.renameEntryE.get(), self.fileOrderE.get())

    def copyFilesE(self):
        fex.processFiles("copy", self.fromPathEntryE.get(), self.toPathEntryE.get(),
                           "." + self.typeEntryE.get(), self.renameEntryE.get(), self.fileOrderE.get())
    
    def zipFilesE(self):
        fex.processFiles("zip", self.fromPathEntryE.get(), self.toPathEntryE.get(),
                           "." + self.typeEntryE.get(), self.renameEntryE.get(), self.fileOrderE.get())
        
    def moveFilesN(self):
        fna.processFiles("move", self.fromPathEntryN.get(), self.toPathEntryN.get(),
                           self.nameEntryN.get(), self.renameEntryN.get(), self.fileOrderN.get())

    def copyFilesN(self):
        fna.processFiles("copy", self.fromPathEntryN.get(), self.toPathEntryN.get(),
                           self.nameEntryN.get(), self.renameEntryN.get(), self.fileOrderN.get())
    
    def zipFilesN(self):
        fna.processFiles("zip", self.fromPathEntryN.get(), self.toPathEntryN.get(),
                           self.nameEntryN.get(), self.renameEntryN.get(), self.fileOrderN.get())

my_gui = MyGUI()
