import csv
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import BayesianEstimator

def BN(DAG):
    data = pd.read_csv('db_after_preprosessing.csv')
    training_data = data[:15068]
    predict_data = data[15068:16952]

    model = BayesianModel(DAG)

    model.fit(data, BayesianEstimator)
    predict_data = predict_data.copy()
    predict_data.drop('song_popularity', axis=1, inplace=True)
    y_pred = model.predict(predict_data)
    print(y_pred)

    with open('predicted_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        predict_data['song_popularity_res'] = y_pred
        writer.writerows(predict_data)


