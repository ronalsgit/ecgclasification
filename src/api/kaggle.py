from src.api import zip
from res.values import value, dir
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

def downloadDataset(path = dir.FILES, extractOriginalZipFile = False, removeOriginalZipFile = False):
    for file_name in value.FILENAMES:
        api.dataset_download_file(value.DATASET, file_name = file_name , path=path)
        if extractOriginalZipFile:
            zip.extractZipFile(path, file_name)
        if removeOriginalZipFile:
            zip.removeZipFile(path, file_name)