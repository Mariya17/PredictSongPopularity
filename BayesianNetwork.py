import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator

def take_only_relevant_features(DAG, db_file):
    all_data = pd.read_csv(db_file)

    data = pd.DataFrame()
    relevant_features = ()
    for tuple_of_two in DAG:
        relevant_features = relevant_features + tuple_of_two

    for column in all_data:
        if column in relevant_features:
            data[column] = all_data[column]
    return data

def BN(DAG, db_file, results_file):

    data = take_only_relevant_features(DAG, db_file)

    training_data = data[:15068]
    predict_data = data[15068:16952]

    model = BayesianModel(DAG)

    model.fit(data, BayesianEstimator)

    predict_data = predict_data.copy()
    predict_data.drop('song_popularity', axis=1, inplace=True)
    y_pred = model.predict(predict_data)
    print(y_pred)

    with open(results_file, 'w', newline='') as file:
        y_pred.to_csv(file)
        # writer = csv.writer(file)
        # predict_data['song_popularity_res'] = y_pred
        # writer.writerows(predict_data)


