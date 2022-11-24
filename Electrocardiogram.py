#from src.api import kaggle
#from res.values import value, path
from src.encryption import encrypt as enc, decrypt as dec, key
from src.clasification import model as mdl, predict as pre, verify as ver, preprosesing as pro
import res.values.value as val
import time

start = time.time()
#kaggle.downloadDataset(extractOriginalZipFile=True,removeOriginalZipFile=True)
end = time.time()
print(val.message.msg("download", end - start))

start = time.time()
#mdl.createModel()
end = time.time()
print(val.message.msg("Model", end - start))

start = time.time()
val.savePickleFile(val.fileName.new_data, [val.loadCsvFile('mitbih_test', 0)[20989]])
end = time.time()
print(val.message.msg("newData", end - start))

start = time.time()
enc_data = enc.encrypt(val.fileName.enc_data, val.loadPickleFile(val.fileName.new_data, 0))
end = time.time()
print(val.message.msg("encrypt", end - start))

start = time.time()
pre_data = pre.predict(val.fileName.pre_data, val.loadPickleFile(val.fileName.enc_data, 0))
end = time.time()
print(val.message.msg("predict", end - start))

start = time.time()
dec_data = dec.decrypt(val.fileName.dec_data, val.loadPickleFile(val.fileName.pre_data, 0))
end = time.time()
print(val.message.msg("decrypt", end - start))

start = time.time()
ver_data = ver.veriffy(val.fileName.ver_data, val.loadPickleFile(val.fileName.dec_data, 0))
end = time.time()
print(val.message.msg("veriffy", end - start))

print(round(ver_data))
print(ver_data)
print(val.loadPickleFile(val.fileName.score))
print(val.loadPickleFile(val.fileName.conf_matrix))
print(val.loadPickleFile(val.fileName.classifi_rpt))