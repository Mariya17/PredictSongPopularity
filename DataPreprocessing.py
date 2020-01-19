import pandas as pd
from collections import OrderedDict
# import Clustering
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import MeanShift, estimate_bandwidth

class DataPeprocessing:
    def __init__(self, DB_file_name, output_file_name):
        self.data_frame = pd.read_csv(DB_file_name)
        self.normalized_data = pd.DataFrame()
        self.output_file_name = output_file_name
        self.header_sublist = ['song_duration_ms',
                               'acousticness',
                               'danceability',
                               'energy',
                               'instrumentalness',
                               'liveness',
                               'loudness',
                               'speechiness',
                               'tempo',
                               'audio_valence']
        # take values as is
        self.new_data_frame = pd.DataFrame({'song_name': self.data_frame['song_name'],
                                       'key': self.data_frame['key'],
                                       'audio_mode': self.data_frame['audio_mode'],
                                       'time_signature': self.data_frame['time_signature']})


    def categorize_value_to_equal_range(self, value, min_val, step_range):
        if value < (min_val + step_range * 1):
            return 0
        elif value < (min_val + step_range * 2):
            return 1
        elif value < (min_val + step_range * 3):
            return 2
        elif value < (min_val + step_range * 4):
            return 3
        elif value < (min_val + step_range * 5):
            return 4
        elif value < (min_val + step_range * 6):
            return 5
        elif value < (min_val + step_range * 7):
            return 6
        else:
            return 7


    # divide data to equal groups
    def data_preprosessing_uniform_distribution(self, column_name, num_of_groups):
        new_column = []
        line_of_value = {}
        column_size = len(self.data_frame[column_name])
        group_size = column_size/num_of_groups

        # create a dictionary of line number=key and value in purpose to recreate original line of each value
        for i in range(column_size):
            line_of_value[i] = self.data_frame[column_name][i]

        # sort a column and divide it to equal groups for uniform distribution
        sorted_values = OrderedDict(sorted(line_of_value.items(),  key=lambda x: x[1]))

        j = 0
        dict_of_new_values = {}
        for group_number in range(num_of_groups):
            for i in range(int(group_size)):
                last_item = sorted_values.popitem()
                dict_of_new_values[last_item[0]] = num_of_groups - group_number - 1
            j += (i + 1)
        while j < column_size:
            j += 1
            last_item = sorted_values.popitem()
            dict_of_new_values[last_item[0]] = 0

        for i in range(column_size):
            new_column.append(dict_of_new_values[i])
        return new_column

    def data_preprosessing_equal_range(self):
        for column in range(len(self.header_sublist)):
            new_column = []
            max_val = max(self.data_frame[self.header_sublist[column]])
            min_val = min(self.data_frame[self.header_sublist[column]])
            step_range = (max_val - min_val)/6
            for i in range(len(self.data_frame[self.header_sublist[column]])):
                new = self.categorize_value_to_equal_range(self.data_frame[self.header_sublist[column]][i], min_val, step_range)
                new_column.append(new)
            self.new_data_frame[self.header_sublist[column]] = new_column


    def meanShift(self, column):
        X = np.reshape(column, (-1, 1))

        bandwidth = estimate_bandwidth(X, quantile=0.1)
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        # ms = MeanShift(bandwidth=None, bin_seeding=True)
        ms.fit(X)
        labels = ms.labels_
        cluster_centers = ms.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        for k in range(n_clusters_):
            my_members = labels == k
            print("cluster {0}: {1}".format(k, X[my_members, 0]))

        return labels, cluster_centers

    """
    Thtis method will prepare the data by three optional methods:
    1. 'MeanShirf' - default
    2. 'Uniform Distribution'
    3. 'Equal Steps'
    """
    def data_preprosessing(self, method = 'MeanShirf'):

        new_column = []


        if method == 'Uniform Distribution':
            for column in range(len(self.header_sublist)):
                self.new_data_frame[self.header_sublist[column]] = self.data_preprosessing_uniform_distribution(self.header_sublist[column], 8)
        elif method == 'Equal Steps':
            self.data_preprosessing_equal_range()
        else:   #'MeanShirf'
            for column in self.header_sublist:
                labled_column, cluster_centers = self.meanShift(self.data_frame[column].values)
                #####################################################################################
                #   we need cluster_centers for future prediction and clustering of a new song     #
                #####################################################################################
                self.new_data_frame[column] = labled_column

        #####################################
        for i in range(len(self.data_frame['song_popularity'])):
            if self.data_frame['song_popularity'][i] < 20:
                new_column.append(0)
            elif self.data_frame['song_popularity'][i] < 40:
                new_column.append(1)
            elif self.data_frame['song_popularity'][i] < 60:
                new_column.append(2)
            elif self.data_frame['song_popularity'][i] < 75:
                new_column.append(3)
            elif self.data_frame['song_popularity'][i] < 85:
                new_column.append(4)
            else:
                new_column.append(5)

        self.new_data_frame['song_popularity'] = new_column

        self.new_data_frame.to_csv(self.output_file_name)

