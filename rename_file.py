import os 
def rename_files(folder_path):
    for filename is os.lisdir(folder_path):
        if filename.endwith(".txt"):
        base = os.path.splitpath(filename)[0]
        old_path=os.path.join(folder_path,filename)
        new_path=os.path.join(folder_path, base + ".log")
        os.rename(old_path,new_path)
rename_files("folder_path")
