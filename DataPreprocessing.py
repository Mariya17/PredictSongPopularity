import pandas as pd
from collections import OrderedDict
import k2
import BayesianNetwork

class DataPeprocessing:
    def __init__(self, DB_file_name, uniform_distribution, output_file_name):
        self.uniform_distribution = uniform_distribution
        self.data_frame = pd.read_csv(DB_file_name)
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
        else:
            return 5


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

    def data_preprosessing(self):
        new_column = []

        if self.uniform_distribution:
            for column in range(len(self.header_sublist)):
                self.new_data_frame[self.header_sublist[column]] = self.data_preprosessing_uniform_distribution(self.header_sublist[column], 8)
        else:
            self.data_preprosessing_equal_range()

        for i in range(len(self.data_frame['song_popularity'])):
            if self.data_frame['song_popularity'][i] < 20:
                new_column.append(0)
            elif self.data_frame['song_popularity'][i] < 40:
                new_column.append(1)
            elif self.data_frame['song_popularity'][i] < 60:
                new_column.append(2)
            elif self.data_frame['song_popularity'][i] < 80:
                new_column.append(3)
            else:
                new_column.append(4)

        self.new_data_frame['song_popularity'] = new_column

        self.new_data_frame.to_csv(self.output_file_name)

