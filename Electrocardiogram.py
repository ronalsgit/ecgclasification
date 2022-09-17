from py.api import kaggle
from res.values import value, path


#TODO CHEK INTERNET CONNECTION IF CONNECTION LOST. DOWNLOAD KAGGLE DATASET NO TESPONS
kaggle.downloadDataset(extractOriginalZipFile=True,removeOriginalZipFile=True)
