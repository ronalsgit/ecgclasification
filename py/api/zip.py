import zipfile
import os

def extractZipFile(path, file_name):
    if os.path.exists(path):
        with zipfile.ZipFile(os.path.join(path , file_name +'.zip'), 'r') as zipref:
            zipref.extractall(path)
    else:
        print("The file does not exist")

def removeZipFile(path, file_name):
    if os.path.exists(os.path.join(path , file_name +'.zip')):
        os.remove(os.path.join(path , file_name +'.zip'))
    else:
        print("The file does not exist")