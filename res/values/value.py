import json
import res.values.path as dir
import pickle
import csv

DATASET          = 'gauravmalik26/food-delivery-dataset'
FILENAMES        = ['test.csv' ]#, 'mitbih_train.csv', 'ptbdb_abnormal.csv', 'ptbdb_normal.csv']
FILENAMES        = FILENAMES[0]
ARCHIVE_TYPE     = '.ZIP'
PICKLE_FILE_TYPE = '.pickle'
CSV_FILE_TYPE    = '.csv'
JSON_FILE_TYPE   = '.Json'
MODEL_FILE_TYPE  = '.mdl'

class fileName():
    key         = 'key'
    encrypted   = 'encrypted'
    decrypted   = 'decrypted'
    
    test_train  = 'XYTest_XYTrain'

    datasetTest = 'mitbih_test'
    datasetTrain= 'mitbih_train'

    coef_       = '_coef'
    intercept_  = '_intercept'

    score       = 'report_score'
    conf_matrix = 'report_confmatrix'
    classifi_rpt= 'report_classif'
    
    tes_data    = 'data_tes'
    new_data    = 'data_new'
    enc_data    = 'data_enc'
    pre_data    = 'data_pre'
    dec_data    = 'data_dec'
    ver_data    = 'data_ver'

class MODE():
    READ       = 'r'
    WRITE      = 'W'
    READ_WRITE = 'rw'
    
class message:
    FILE_NOT_EXIST = 'The file does not exist'
    def msg(param1, param2):
        return 'Time execution of {0} data is : {1:.12f}'.format(param1, param2)

def savePickleFile(fileName, data):
    with open(f'{dir.PICKLE}{fileName}{PICKLE_FILE_TYPE}', 'wb') as f:pickle.dump(data, f)
    
def loadPickleFile(fileName, _print=0):
    with open(f'{dir.PICKLE}{fileName}{PICKLE_FILE_TYPE}', 'rb') as f:
        datas = pickle.load(f)
        if _print : print(datas)
    return datas

def saveJsonFile(fileName, data):
    with open(f'{dir.PICKLE}{fileName}{JSON_FILE_TYPE}', 'w') as f:json.dump(data, f)
    
def loadJsonFile(fileName):
    with open(f'{dir.PICKLE}{fileName}{JSON_FILE_TYPE}', 'r') as f:return json.load(f)

def saveModelFile(fileName, data):
    with open(f'{dir.MODEL}{fileName}{MODEL_FILE_TYPE}', 'wb') as f:pickle.dump(data, f)
    
def loadModelFile(fileName):
    with open(f'{dir.MODEL}{fileName}{MODEL_FILE_TYPE}', 'rb') as f:return pickle.load(f)
    
def loadCsvFile(fileName, _print=0):
    datas = []
    with open(f'{dir.FILES}{fileName}{CSV_FILE_TYPE}') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
        for row in reader: # each row is a list
            datas.append(row)
            if _print : print(datas)
    
    return datas