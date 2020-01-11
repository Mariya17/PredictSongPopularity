import pandas as pd
from collections import OrderedDict
import k2
import BayesianNetwork
import DataPreprocessing


class PredictSongPopularity:
    def __init__(self):
        self.ordered_list = ['tempo',
                             'audio_mode',
                             'song_duration_ms',
                             'key',
                             'time_signature',
                             'acousticness',
                             'instrumentalness',
                             'liveness',
                             'loudness',
                             'speechiness',
                             'audio_valence',
                             'danceability',
                             'energy',
                             'song_popularity']


        self.db_file_name = 'song_data.csv'

        self.processed_data_file_name = 'db_after_preprosessing.csv'
        self.DAG = []

    def predict(self):
        data_base = DataPreprocessing.DataPeprocessing(self.db_file_name, False, self.processed_data_file_name)
        data_base.data_preprosessing()
        K2Algorithm = k2.K2(self.ordered_list, self.processed_data_file_name)

        # DAG_uniform_distrebution = 	[('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('tempo', 'time_signature'), ('acousticness', 'instrumentalness'), ('acousticness', 'loudness'), ('instrumentalness', 'loudness'), ('tempo', 'speechiness'), ('audio_valence', 'danceability'), ('tempo', 'danceability'), ('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('acousticness', 'song_popularity')]
        # self.DAG = DAG_uniform_distrebution

        self.DAG = K2Algorithm.k2()

        BayesianNetwork.BN(self.DAG)


def main():
    predict = PredictSongPopularity()
    predict.predict()


if __name__ == '__main__':
    main()
