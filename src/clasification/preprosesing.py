def padding(arr, max_len):
    while len(arr) != max_len:
        if len(arr) > max_len: arr = arr[:max_len]
        else: arr.append(0)
    return arr

def getDataset(data):
    values, labels = [], []
    for x in range(len(data)):
        values.append(data[x][:-1])
        #if data less then 0 then labels equals to 0 otherwise equals to 1
        labels.append(1 if data[x][-1] > 0 else 0)
        _max_len = max([len(i) for i in values]) #Array terpanjang
        values = [padding(i, _max_len) for i in values]
    
    return values, labels
