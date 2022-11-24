import res.values.value as val
import phe as paillier
import numpy as np
from src.encryption import decrypt as dec
import time

def paillierEncNum(data, encrypt = True):
    pub_key = paillier.PaillierPublicKey(n=int(data['public_key']['n']))
    listData =[]
    for n in range(len(data['value'])):
        for x in range(len(data['value'][n])):
            list = paillier.EncryptedNumber(pub_key, int(data['value'][n][x][0]), int(data['value'][n][x][1]))
            listData.append(list if encrypt else dec.decrypt(None, list))

    return listData

def predict(path, newData):
    coef_       = val.loadPickleFile(val.fileName.coef_)
    coef_       = np.array(paillierEncNum(coef_, False))
    
    intercept_  = val.loadPickleFile(val.fileName.intercept_)
    intercept_  = np.array(paillierEncNum(intercept_))[0]
    
    enc_        = newData
    enc_        = np.array(paillierEncNum(enc_))[:-1]

    start = time.time()
    result_enc    = -1 * (np.dot(enc_, coef_) + intercept_)
    end = time.time()
    print(val.message.msg("predict", end - start))

    val.savePickleFile(path, result_enc)

    return result_enc
