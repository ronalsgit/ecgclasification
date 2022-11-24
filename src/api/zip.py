import zipfile
import os
from res.values import value

def extractZipFile(path, file_name):
    if os.path.exists(path):
        with zipfile.ZipFile(os.path.join(path , file_name + value.ARCHIVE_TYPE ), value.MODE.READ ) as zipref:
            zipref.extractall(path)
    else:
        print(value.message.FILE_NOT_EXIST)

def removeZipFile(path, file_name):
    if os.path.exists(os.path.join(path , file_name + value.ARCHIVE_TYPE)):
        os.remove(os.path.join(path , file_name + value.ARCHIVE_TYPE))
    else:
        print(value.message.FILE_NOT_EXIST)