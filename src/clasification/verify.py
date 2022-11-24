
import res.values.value as val
import math

def veriffy(path, data):

    verify = 1 / (1 + (math.e ** data))

    val.savePickleFile(path, verify)



    return verify