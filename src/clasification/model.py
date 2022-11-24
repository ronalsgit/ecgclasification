from sklearn.utils.validation import check_is_fitted
from sklearn.linear_model import LogisticRegression
import res.values.value as val
from src.clasification import preprosesing as pro
from src.encryption import encrypt as enc
from sklearn import metrics

def loadDataset():
    X_test , y_test = pro.getDataset(val.loadCsvFile(val.fileName.datasetTest)) 
    X_train, y_train = pro.getDataset(val.loadCsvFile(val.fileName.datasetTrain)) 
    val.savePickleFile(val.fileName.test_train, (X_train, X_test, y_train, y_test))

def createModel():  
    #loadDataset()
    X_train, X_test, y_train, y_test = val.loadPickleFile(val.fileName.test_train)
    model = LogisticRegression(C=10,random_state=0,penalty='l1',solver='liblinear')
    model.fit(X_train, y_train)
    check_is_fitted(model)
    val.saveModelFile('model',model)

    #mean accuracy from X_test And Y_test
    model = val.loadModelFile('model')
    predictions = model.predict(X_test) 

    score = model.score(X_test, y_test) 
    conf_matrix = metrics.confusion_matrix(y_test, predictions)
    classifi_rpt = metrics.classification_report(y_test, predictions)

    #encrypt and save coefision and intercept to pickle file
    enc.encrypt(val.fileName.coef_, [x for x in model.coef_]) 
    enc.encrypt(val.fileName.intercept_, [model.intercept_])
    val.savePickleFile(val.fileName.score, score)
    val.savePickleFile(val.fileName.conf_matrix, conf_matrix)
    val.savePickleFile(val.fileName.classifi_rpt, classifi_rpt)
