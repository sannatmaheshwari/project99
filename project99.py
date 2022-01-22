import os
import shutil
import time
def main():
    deletedfoldersCount = 0
    deletedfilesCount = 0
    path = "/PATH_TO_DELETE"
    days = 30
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolder,folder,files in os.walk(path):
            if seconds>=get_file_or_folder_age(rootfolder):
                remove_folder(rootfolder)
                deletedfoldersCount+=1
                break
            else:
                for folder in folder:
                    folderpath = os.path.join(rootfolder,folder)
                    if seconds>=get_file_or_folder_age(folderpath):
                        remove_folder(folderpath)
                        deletedfoldersCount+=1
                for file in files:
                    filepath = os.path.join(rootfolder,file)
                    if seconds>=get_file_or_folder_age(filepath):
                        remove_file(filepath)
                        deletedfilesCount+=1
main()