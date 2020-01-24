import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator


class BN:
    def __init__(self, DAG):
        self.data = []
        self.model = BayesianModel(DAG)

    def take_only_relevant_features(self, DAG, db_file):
        all_data = pd.read_csv(db_file)

        data = pd.DataFrame()
        relevant_features = ()
        for tuple_of_two in DAG:
            relevant_features = relevant_features + tuple_of_two

        for column in all_data:
            if column in relevant_features:
                data[column] = all_data[column]
        return data

    def BNLearning(self, DAG, db_file):
        self.data = self.take_only_relevant_features(DAG, db_file)
        self.model = BayesianModel(DAG)

        self.model.fit(self.data, BayesianEstimator)

    def BNTesting(self, results_file):
        # separate data for test
        training_part = int(0.8 * len(self.data))
        testing_data = self.data[training_part:]

        # predict
        predict_data = testing_data.copy()
        predict_data.drop('song_popularity', axis=1, inplace=True)
        y_pred = self.model.predict(predict_data)

        with open(results_file, 'w', newline='') as file:
            y_pred.to_csv(file)

    def BNForOneSong(self, DAG, db_file, results_file, songFile):
        data = self.take_only_relevant_features(DAG, db_file)
        dataToPredictRF = self.take_only_relevant_features(DAG, songFile)
        dataToPredict = pd.read_csv(songFile)

        model = BayesianModel(DAG)

        model.fit(data, BayesianEstimator)

        dataToPredictRF = dataToPredictRF.copy()
        y_pred = model.predict(dataToPredictRF)
        # print(y_pred)

        with open(results_file, 'w', newline='') as file:
            y_pred.to_csv(file)

        return y_pred['song_popularity'][0]
