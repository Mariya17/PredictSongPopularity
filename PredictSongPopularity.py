import pandas as pd
from collections import OrderedDict
import k2
import BayesianNetwork
import DataPreprocessing
import Measurements
from Const import Files


class PredictSongPopularity:
    def __init__(self):
        # self.ordered_list = [
        #                      'tempo',
		# 		        	 'audio_mode',
		# 		        	 'song_duration_ms',
		# 		        	 'key',
		# 		        	 'time_signature',
		# 		        	 'acousticness',
		# 		        	 'instrumentalness',
		# 		        	 'liveness','loudness',
		# 		        	 'speechiness',
		# 		        	 'audio_valence',
		# 		        	 'danceability',
		# 		        	 'energy',
        #                      'song_popularity']

        self.db_file_name = Files.DB_BEFORE_PREPROSSECCING
        self.predicted_results_file_name = Files.PREDICT_RESULTS
        self.predicted_single_song_result_file_name = Files.PREDICT_RESULTS_SINGLE_SONG
        self.DAG_File = Files.DAG
        self.processed_data_file_name = Files.DB_AFTER_PREPROSSECCING
        self.DAG = []
        self.BN = BayesianNetwork.BN(self.DAG)

    ####################### Separated Predicting #######################
    #     1.
    def preprocessing(self):
        data_base = DataPreprocessing.DataPeprocessing(self.db_file_name, self.processed_data_file_name)
        """
        1. 'MeanShirf' - default
        2. 'Uniform Distribution'
        3. 'Equal Steps'
        """
        data_base.data_preprosessing('Equal Steps')
    #     2.
    def performK2(self):
        K2Algorithm = k2.K2(Files.K2_INPUT, self.processed_data_file_name)
        self.DAG = K2Algorithm.k2()
        str = ''
        if not('song_popularity' in self.DAG):
            str = 'Can not build a model with current K2 Input.\nPlease try another one. '
        self.convertDagToFile()
        return str
    #    3.
    def bayesianLearning(self):
        self.BN.BNLearning(self.DAG, self.processed_data_file_name)
    #    4.
    def bayesianTesting(self):
        self.BN.BNTesting(self.predicted_results_file_name)
    #    5.
    def mseMeasure(self):
        mse = Measurements.mse(self.processed_data_file_name, self.predicted_results_file_name)
        str = "MSE is: {0}\n".format(mse)
        print(str)
        return str

    #    TODO: Galit - add print to graph file for the current div and type of preprosseccing

    #    6.
    def errorInPresents(self):
        errorRate = Measurements.errorRate(self.processed_data_file_name, self.predicted_results_file_name)
        str = "Accuracy of prediction is: {0}%\n".format(100 - errorRate)
        print(str)
        return str

    # def predict(self):
        # print('Started learning\n')
        # data_base = DataPreprocessing.DataPeprocessing(self.db_file_name, self.processed_data_file_name)
        # """
        # 1. 'MeanShirf' - default
        # 2. 'Uniform Distribution'
        # 3. 'Equal Steps'
        # """
        # data_base.data_preprosessing('Equal Steps')
        # K2Algorithm = k2.K2(self.ordered_list, self.processed_data_file_name)
        #
        # # # DAG_uniform_distrebution = 	[('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('tempo', 'time_signature'), ('acousticness', 'instrumentalness'), ('song_duration_ms', 'instrumentalness'), ('acousticness', 'loudness'), ('instrumentalness', 'loudness'), ('acousticness', 'speechiness'), ('audio_valence', 'danceability'), ('tempo', 'danceability'), ('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('loudness', 'song_popularity'), ('energy', 'song_popularity')]
        # # DAG_MeanShift = [('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('audio_mode', 'time_signature'), ('acousticness', 'instrumentalness'), ('song_duration_ms', 'instrumentalness'), ('acousticness', 'loudness'), ('tempo', 'danceability'), ('audio_valence', 'danceability'), ('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('acousticness', 'song_popularity')]
        # # # self.DAG = DAG_uniform_distrebution
        #
        # # DAG_MeanShift = [('tempo', 'audio_mode'), ('audio_mode', 'song_duration_ms'), ('tempo', 'time_signature'),('acousticness', 'instrumentalness'), ('acousticness', 'loudness'), ('instrumentalness', 'loudness'),('speechiness', 'danceability'), ('instrumentalness', 'song_popularity'), ('loudness', 'song_popularity')]
        # #self.DAG = DAG_MeanShift
        #
        # self.DAG = K2Algorithm.k2()
        # self.convertDagToFile()
        # DagTest = self.convertFileToDAG()

        # BayesianNetwork.BN(self.DAG, self.processed_data_file_name, self.predicted_results_file_name)

        # mse = Measurements.mse(self.processed_data_file_name, self.predicted_results_file_name)
        # print("MSE is: {0}%".format(mse))
        # errorRate = Measurements.errorRate(self.processed_data_file_name, self.predicted_results_file_name)
        # print("Error Rate is: {0}%".format(errorRate))

    def convertDagToFile(self):
        parent = []
        child = []

        for tuple_of_two in self.DAG:
            parent.append(tuple_of_two[0])
            child.append(tuple_of_two[1])

        dictOfColumns = {'Parent': parent, 'Child': child}
        df = pd.DataFrame(dictOfColumns, columns=['Parent', 'Child'])
        fileToExe = df.to_csv(r''+Files.DAG, index=None, header=True)

    def convertFileToDAG(self):
        data = pd.read_csv(self.DAG_File, header=None)

        rowsCsv, colCsv = data.shape
        dag = []
        for i in range(1, rowsCsv):
          dag.append((data[0][i], data[1][i]))

        return dag

    def predictSingle(self, songFile):
        data_base = DataPreprocessing.DataPeprocessing(self.db_file_name, self.processed_data_file_name)
        data_base.data_preprosessing('Equal Steps')
        self.DAG = self.convertFileToDAG()
        bn = BayesianNetwork.BN(self.DAG)
        res = bn.BNForOneSong(self.DAG, self.processed_data_file_name, self.predicted_results_file_name, songFile)
        print(res)
        return res


# def main():
#     predict = PredictSongPopularity()
#     predict.predict()
#
# def main():
#     Measurements.createGraph()
#
# # def main():
# #     predict = PredictSongPopularity()
# #     predict.predictSingle("C:/galitProject/PredictSongPopularity/testPredictSingleSong.csv")
# #
# #
# if __name__ == '__main__':
#     main()
