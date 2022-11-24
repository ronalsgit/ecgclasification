import time
import res.values.value as val

def timeExecution(func, name = ''):

    start = time.time()
    func
    end = time.time()
    
    print(val.message.msg(name, end - start))
