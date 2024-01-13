import os
import datetime
import zipfile
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import shutil

class MyGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("630x800+100+100")
        self.main_window.title("File Manager")
        
        # Frames
        self.frame1 = Frame(self.main_window, width=630, height=160, bd=2, relief="solid")
        self.frame1.place(x=0, y=0)
        self.frame2 = Frame(self.main_window, width=630, height=160, bd=2, relief="solid")
        self.frame2.place(x=0, y=200)
        
        
        # Title
        self.moveLabel = Label(self.frame1, text="Move File", font=("Arial", 20), bg="black")
        self.moveLabel.place(x=20, y=0)
        
        
        # Paths
        self.fromPathLabel = Label(self.frame1, text="From", font=14)
        self.fromPathLabel.place(x=20, y=40)
        self.fromPathEntry = Entry(self.frame1, width=35, font=14)
        self.fromPathEntry.place(x=60, y=40)

        self.toPathLabel = Label(self.frame1, text="To", font=14)
        self.toPathLabel.place(x=20, y=70)
        self.toPathEntry = Entry(self.frame1, width=35, font=14)
        self.toPathEntry.place(x=60, y=70)
        
        
        # file extension
        self.typeLabel = Label(self.frame1, text="File Extension", font=14)
        self.typeLabel.place(x=410, y=40)
        self.typeEntry = Entry(self.frame1, width=10, font=14)
        self.typeEntry.place(x=500, y=40)
        
        
        # Rename
        self.renameLabel = Label(self.frame1, text="Rename(optional)", font=14)
        self.renameLabel.place(x=20, y=120)
        self.renameEntry = Entry(self.frame1, width=10, font=14)
        self.renameEntry.place(x=130, y=120)
        
        
        # buttons
        self.moveFileBtn = Button(self.frame1, text="Move", font=14, command=self.moveFiles)
        self.moveFileBtn.place(x=450, y=120)
        self.copyFileBtn = Button(self.frame1, text="Copy", font=14, command=self.copyFiles)
        self.copyFileBtn.place(x=530, y=120)
        self.zipFileBtn = Button(self.frame1, text="Zip", font=14, command=self.zipFiles)
        self.zipFileBtn.place(x=380, y=120)

        
        self.fileOrder=StringVar()
        self.fileOrder.set("asc")
        self.ascOrder=Radiobutton(self.frame1, text="Ascending", font=14, variable=self.fileOrder, value="asc")
        self.ascOrder.place(x=400, y=70)
        self.desOrder=Radiobutton(self.frame1, text="Descending", font=14, variable=self.fileOrder, value="desc")
        self.desOrder.place(x=500, y=70)
        mainloop()



    def getFileCreationTime(self, filePath):
        return os.stat(filePath).st_birthtime
    
        
    def processFiles(self, action):
        pathFrom = self.fromPathEntry.get()
        pathTo = self.toPathEntry.get()
        fileType = "." + self.typeEntry.get()
        rename = self.renameEntry.get()
        count = 0

        if pathFrom and pathTo and fileType:

            filesToMove = []

            for path, dirs, files in os.walk(pathFrom):
                for file in files:
                    filePath = os.path.join(pathFrom, file)
                    fileName, fileExtension = os.path.splitext(file)

                    if fileExtension == fileType:
                        filesToMove.append(filePath)
            
            if self.fileOrder.get() == "asc":
                filesToMove.sort(key=self.getFileCreationTime)
            elif self.fileOrder.get() == "desc":
                filesToMove.sort(key=self.getFileCreationTime, reverse=True)
            
            for filePath in filesToMove:
                count += 1

                fileName, fileExtension = os.path.splitext(os.path.basename(filePath))

                if rename:
                    newFileName = f"{rename}_{count}"
                else:
                    newFileName = fileName

                newPath = os.path.join(pathTo, f"{newFileName}{fileExtension}")
  
                if action == "move":
                    shutil.move(filePath, newPath)
                elif action == "copy":
                    shutil.copy(filePath, newPath)
                elif action == "zip":
                    zipFilePath = os.path.join(pathTo, f"{self.typeEntry.get()}_files.zip")
                    with zipfile.ZipFile(zipFilePath, "w", compression=zipfile.ZIP_DEFLATED) as myZip:
                        for file in filesToMove:
                            myZip.write(file)
                        
            if action == "move":
                showinfo("Success", f"{count} files moved successfully.")
            elif action == "copy":
                showinfo("Success", f"{count} files copied successfully.")
            elif action == "zip":
                showinfo("Success", f"{count} files zipped successfully.")
        else:
            showerror("Error", "Please fill in all the required fields.")
            
    def moveFiles(self):
        self.processFiles("move")

    def copyFiles(self):
        self.processFiles("copy")
    
    def zipFiles(self):
        self.processFiles("zip")

my_gui = MyGUI()
