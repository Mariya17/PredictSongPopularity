import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import Const

def mse(exceptedPath, testPredRes):
    dataDB = pd.read_csv(exceptedPath)
    dataTstsRes = pd.read_csv(testPredRes)

    traning_part = int(0.8 * len(dataDB))
    # Given values
    Y_true = [dataDB['song_popularity'][traning_part:]]  # Y_true = Y (original values)

    # calculated values
    Y_pred = [dataTstsRes['song_popularity']]  # Y_pred = Y'
    print('{0} : {1}'.format('Y_pred', Y_pred))

    # Calculation of Mean Squared Error (MSE)
    mse = mean_squared_error(Y_true, Y_pred)

    return mse

def errorRate(exceptedPath, testPredRes):
    dataDB = pd.read_csv(exceptedPath)
    dataTstsRes = pd.read_csv(testPredRes)

    rowsCsv, colCsv = dataDB.shape
    errorRate = 0
    i = 0
    traning_part = int(0.8 * rowsCsv)
    len = rowsCsv - traning_part

    divN = 1 / len
    for expected in dataDB['song_popularity'][traning_part:]:

        pred = dataTstsRes['song_popularity'][i]
        temp = (abs(expected - pred) / (expected + 1)) * divN
        errorRate += temp
        i += 1

    errorRate *= 100

    return errorRate

def createGraph(fileType):
    x, y = convertFileTofraph(Const.Files.GRAPH, fileType)
    for i in y:
        i = 100 - int(i)
    plt.plot(x, y,
             color='green',
             marker='o',
             linestyle='dashed',
             linewidth=2,
             markersize=4)
    plt.title(fileType)
    plt.xlabel('div')
    plt.ylabel('success')
    plt.show()

def convertFileTofraph(graph_file, fileType):
    data = pd.read_csv(graph_file)

    rowsCsv, colCsv = data.shape
    x = [data['x'][i] for i in range(0, rowsCsv)]
    y = [data[fileType][i] for i in range(0, rowsCsv)]

    return x, y

def addToGraphFile():
    pass
