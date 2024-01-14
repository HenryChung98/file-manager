import os
import shutil
import zipfile
from tkinter.messagebox import showinfo, showerror, showwarning

# sort by birth time
def getFileCreationTime(filePath):
    return os.stat(filePath).st_birthtime

def processFiles(action, fromPath, toPath, fileType, rename, fileOrder):
    count = 0
    
    # check filled
    if fromPath and toPath and fileType:

        filesToMove = []

        for path, dirs, files in os.walk(fromPath):
            for file in files:
                filePath = os.path.join(fromPath, file)
                fileName, fileExtension = os.path.splitext(file)
                
                # check name with startswith
                if fileName.startswith(fileType):
                    filesToMove.append(filePath)

        # sort the list
        if fileOrder == "asc":
            filesToMove.sort(key=getFileCreationTime)
        elif fileOrder == "desc":
            filesToMove.sort(key=getFileCreationTime, reverse=True)
        
        
        for filePath in filesToMove:
            count += 1

            fileName, fileExtension = os.path.splitext(os.path.basename(filePath))
            
            # check rename entry filled
            if rename:
                newFileName = f"{rename}_{count}"
            else:
                newFileName = fileName

            newPath = os.path.join(toPath, f"{newFileName}{fileExtension}")
            
            
            # check the file name is duplicated
            dCount = 0
            while os.path.exists(newPath):
                dCount += 1
                newFileName = f"renameIt_{dCount}" if rename else f"{fileName}_{dCount}"
                newPath = os.path.join(toPath, f"{newFileName}{fileExtension}")
                
                
            # check the action
            if action == "move":
                shutil.move(filePath, newPath)
            elif action == "copy":
                shutil.copy(filePath, newPath)
            elif action == "zip":
                zipFilePath = os.path.join(toPath, f"{fileType}_files.zip")
                with zipfile.ZipFile(zipFilePath, "w", compression=zipfile.ZIP_DEFLATED) as myZip:
                    for file in filesToMove:
                        myZip.write(file)
 
        # output
        if action == "move":
            if dCount != 0:
                showwarning("Warning", f"CAREFUL!!\n {dCount} files have duplicated name")
            showinfo("Success", f"{count} files moved successfully.")
        elif action == "copy":
            if dCount != 0:
                showwarning("Warning", f"CAREFUL!!\n {dCount} files have duplicated name")
            showinfo("Success", f"{count} files copied successfully.")
        elif action == "zip":
            if dCount != 0:
                showwarning("Warning", f"CAREFUL!!\n {dCount} files have duplicated name")
            showinfo("Success", f"{count} files zipped successfully.")
    else:
        showerror("Error", "Please fill in all the required fields.")

