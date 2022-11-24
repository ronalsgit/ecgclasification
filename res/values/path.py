import os

path = os.getcwd()

MANIFEST   = os.path.normpath(path + "/manifest") + '/'

PY         = os.path.normpath(path + "/py")
DIR        = os.path.normpath(path + "/py/constatn")
API        = os.path.normpath(path + "/py/api")
CLASIFFY   = os.path.normpath(path + "/py/clasiffy")
ENCRYPTION = os.path.normpath(path + "/py/encryption")

RES        = os.path.normpath(path + "/res")
DATASET    = os.path.normpath(path + "/res/dataset")
FILES      = os.path.normpath(path + "/res/dataset/data")+ '/'
MODEL      = os.path.normpath(path + "/res/dataset/model")+ '/'
PICKLE     = os.path.normpath(path + "/res/dataset/pickle")+ '/'
 
DRAWABLE   = os.path.normpath(path + "/res/drawable")
VALUES     = os.path.normpath(path + "/res/values")