import pandas as pd
from collections import OrderedDict
import k2
import BayesianNetwork
import DataPreprocessing
import Measurements


class PredictSongPopularity:
    def __init__(self):
        self.ordered_list = [
                             'tempo',
				        	 'audio_mode',
				        	 'song_duration_ms',
				        	 'key',
				        	 'time_signature',
				        	 'acousticness',
				        	 'instrumentalness',
				        	 'liveness','loudness',
				        	 'speechiness',
				        	 'audio_valence',
				        	 'danceability',
				        	 'energy',
                             'song_popularity']


        self.db_file_name = 'song_data.csv'
        self.predicted_results_file_name = 'predicted_results.csv'

        self.processed_data_file_name = 'db_after_preprosessing.csv'
        self.DAG = []

    def predict(self):
        print('Started learning\n')
        data_base = DataPreprocessing.DataPeprocessing(self.db_file_name, self.processed_data_file_name)
        """
        1. 'MeanShirf' - default
        2. 'Uniform Distribution'
        3. 'Equal Steps'
        """
        data_base.data_preprosessing('Equal Steps')
        K2Algorithm = k2.K2(self.ordered_list, self.processed_data_file_name)

        # # DAG_uniform_distrebution = 	[('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('tempo', 'time_signature'), ('acousticness', 'instrumentalness'), ('song_duration_ms', 'instrumentalness'), ('acousticness', 'loudness'), ('instrumentalness', 'loudness'), ('acousticness', 'speechiness'), ('audio_valence', 'danceability'), ('tempo', 'danceability'), ('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('loudness', 'song_popularity'), ('energy', 'song_popularity')]
        # DAG_MeanShift = [('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('audio_mode', 'time_signature'), ('acousticness', 'instrumentalness'), ('song_duration_ms', 'instrumentalness'), ('acousticness', 'loudness'), ('tempo', 'danceability'), ('audio_valence', 'danceability'), ('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('acousticness', 'song_popularity')]
        # # self.DAG = DAG_uniform_distrebution

        # DAG_MeanShift = [('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('tempo', 'time_signature'),('acousticness', 'instrumentalness'), ('acousticness', 'loudness'), ('instrumentalness', 'loudness'),('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('loudness', 'song_popularity')]
        #self.DAG = DAG_MeanShift

        self.DAG = K2Algorithm.k2()

        BayesianNetwork.BN(self.DAG, self.processed_data_file_name, self.predicted_results_file_name)

        mse = Measurements.mse(self.processed_data_file_name, self.predicted_results_file_name)
        print("MSE is: {0}%".format(mse))
        errorRate = Measurements.errorRate(self.processed_data_file_name, self.predicted_results_file_name)
        print("Error Rate is: {0}%".format(errorRate))


def main():
    predict = PredictSongPopularity()
    predict.predict()


if __name__ == '__main__':
    main()
