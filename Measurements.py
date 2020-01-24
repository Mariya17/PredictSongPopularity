from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
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

# def createGraph(fileType):
#     x, y = convertFileTofraph(Const.Files.GRAPH, fileType)
#     for i in y:
#         i = 100 - int(i)
#     plt.plot(x, y,
#              color='green',ע
#              marker='o',
#              linestyle='dashed',
#              linewidth=2,
#              markersize=4)
#     plt.title(fileType)
#     plt.xlabel('div')
#     plt.ylabel('success')
#     plt.show()

def createGraph():
    data = pd.read_csv(Const.Files.GRAPH)
    rowsCsv, colCsv = data.shape
    x = [data['x'][i] for i in range(0, rowsCsv)]
    errorRateList = [data[Const.GraphType.ERROR_RATE][i] for i in range(0, rowsCsv)]
    mseList = [data[Const.GraphType.MSE][i] for i in range(0, rowsCsv)]
    for i in errorRateList:
        i = 100 - int(i)
    # width of the bars
    barWidth = 0.1

    # The x position of bars
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]

    # Create blue bars
    plt.bar(r1, mseList, width=barWidth, color='green', edgecolor='black', capsize=7, label='MSE')

    # Create cyan bars
    plt.bar(r2, errorRateList, width=barWidth, color='blue', edgecolor='black', capsize=7, label='Accuracy')

    # general layout
    plt.xticks([r + barWidth for r in range(len(mseList))], x)
    plt.legend()

    # Show graphic
    plt.suptitle("Uniform method")
    plt.show()



def convertFileTofraph(graph_file, fileType):
    data = pd.read_csv(graph_file)

    rowsCsv, colCsv = data.shape
    x = [data['x'][i] for i in range(0, rowsCsv)]
    y = [data[fileType][i] for i in range(0, rowsCsv)]

    return x, y

def addToGraphFile(mse, error):
    data = pd.read_csv(Const.Files.GRAPH)
    rowsCsv, colCsv = data.shape
    x = [data['x'][i] for i in range(0, rowsCsv)]
    errorRateList = [data[Const.GraphType.ERROR_RATE][i] for i in range(0, rowsCsv)]
    mseList = [data[Const.GraphType.MSE][i] for i in range(0, rowsCsv)]
    index = rowsCsv
    if data['x'][0] == "empty":
        x = x[:-1]
        mseList = mseList[:-1]
        errorRateList = errorRateList[:-1]
    else:
        for i in range(0, rowsCsv):
            if int(x[i]) >= Const.PreprocessingTypes.NUMBER_TO_DIV:
                index = i
                break
    x.insert(index, str(Const.PreprocessingTypes.NUMBER_TO_DIV))
    errorRateList.insert(index, str(error))
    mseList.insert(index, str(mse))

    dictOfColumns = {'x': x, Const.GraphType.ERROR_RATE: errorRateList, Const.GraphType.MSE: mseList}
    df = pd.DataFrame(dictOfColumns, columns=['x', Const.GraphType.ERROR_RATE, Const.GraphType.MSE])
    fileToExe = df.to_csv(r'' + Const.Files.GRAPH, index=None, header=True)

