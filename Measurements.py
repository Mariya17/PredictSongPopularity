import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

def mse(exceptedPath, testPredRes):
    dataDB = pd.read_csv(exceptedPath)
    # print ('PATH_OF_DB read successfully')
    dataTstsRes = pd.read_csv(testPredRes)
    # print ('PATH_OF_TESTS_RES read successfully')

    # Given values
    Y_true = [dataDB['song_popularity'][15068:16952]]  # Y_true = Y (original values)
    # Y_true = [dataDB['song_popularity']]  # Y_true = Y (original values)

    # calculated values
    Y_pred = [dataTstsRes['song_popularity']]  # Y_pred = Y'
    print('{0} : {1}'.format('Y_pred', Y_pred))

    # Calculation of Mean Squared Error (MSE)
    mse = mean_squared_error(Y_true, Y_pred)

    return mse

def errorRate(exceptedPath, testPredRes):
    dataDB = pd.read_csv(exceptedPath)
    # print ('PATH_OF_DB read successfully')
    dataTstsRes = pd.read_csv(testPredRes)
    # print ('PATH_OF_TESTS_RES read successfully')

    errorRate = 0
    i = 0
    len = 16952.0 - 15068.0
    # len = 5.0
    divN = 1 / len
    for expected in dataDB['song_popularity'][15068:16952]:
        # for expected in dataDB['song_popularity'][0:5]:
        # print "{0} : {1} - {2}".format(i, expected, dataTstsRes['song_popularity'][i])
        pred = dataTstsRes['song_popularity'][i]
        temp = (abs(expected - pred) / (expected + 1)) * divN
        errorRate += temp
        i += 1

    errorRate *= 100

    return errorRate

def createGraph(yValues, xVlaues):
    plt.plot(xVlaues, yValues,
             color='green',
             marker='o',
             linestyle='dashed',
             linewidth=2,
             markersize=4)


    plt.title('A tale of 2 subplots')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')
    plt.show()

