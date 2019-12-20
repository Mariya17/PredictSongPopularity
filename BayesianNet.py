import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import BayesianEstimator
from collections import OrderedDict

def BayesianModel():
    data = pd.DataFrame(data={'fruit': ["banana", "apple", "banana", "apple", "banana","apple", "banana",
                                        "apple", "apple", "apple", "banana", "banana", "apple", "banana",],
                              'tasty': ["yes", "no", "yes", "yes", "yes", "yes", "yes",
                                        "yes", "yes", "yes", "yes", "no", "no", "no"],
                              'size': ["large", "large", "large", "small", "large", "large", "large",
                                        "small", "large", "large", "large", "large", "small", "small"]})
    print(data)

    model = BayesianModel([('fruit', 'tasty'), ('size', 'tasty')])  # fruit -> tasty <- size

    pe = ParameterEstimator(model, data)
    print("\n", pe.state_counts('fruit'))  # unconditional
    print("\n", pe.state_counts('tasty'))  # conditional on fruit and size

    est = BayesianEstimator(model, data)

    print(est.estimate_cpd('tasty', prior_type='BDeu', equivalent_sample_size=10))


def categorize_value_to_equal_range(value, min_val, step_range):
    if value < (min_val + step_range * 0):
        return 0
    elif value < (min_val + step_range * 1):
        return 1
    elif value < (min_val + step_range * 2):
        return 2
    elif value < (min_val + step_range * 3):
        return 3
    elif value < (min_val + step_range * 4):
        return 4
    elif value < (min_val + step_range * 5):
        return 5
    else:
        return 6

def data_preprosessing():
    uniform_distribution = True
    data_frame = pd.read_csv('Short_song_data.csv')

    header_list = ["song_name","song_popularity","song_duration_ms","acousticness","danceability","energy","instrumentalness","key","liveness","loudness","audio_mode","speechiness","tempo","time_signature","audio_valence"]
    header_sublist = ["song_duration_ms","acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","tempo","audio_valence"]
    #take values as is
    new_data_frame = pd.DataFrame({'song_name': data_frame['song_name'],
                                   'key': data_frame['key'],
                                   'audio_mode': data_frame['audio_mode'],
                                   'time_signature': data_frame['time_signature']})

    new_column = []
    for i in range(len(data_frame['song_popularity'])):
        if data_frame['song_popularity'][i] < 20:
            new_column.append(0)
        elif data_frame['song_popularity'][i] < 40:
            new_column.append(1)
        elif data_frame['song_popularity'][i] < 60:
            new_column.append(2)
        elif data_frame['song_popularity'][i] < 80:
            new_column.append(3)
        else:
            new_column.append(4)

    new_data_frame['song_popularity'] = new_column

    if uniform_distribution:
        for column in range(len(header_sublist)):
            new_data_frame[header_sublist[column]] = data_preprosessing_uniform_distribution(data_frame, header_sublist[column],8)
        new_data_frame.to_csv('db_uniform_distribution.csv')
    else:
        data_preprosessing_equal_range(data_frame, new_data_frame, header_sublist)
        new_data_frame.to_csv('db_equal_steps.csv')

#divide data to equal groups
def data_preprosessing_uniform_distribution(data_frame, column_name, num_of_groups ):
    new_column = []
    line_of_value = {}
    column_size = len(data_frame[column_name])
    group_size = column_size/num_of_groups

    #create a dictionary of line number=key and value in purpose to recreate original line of each value
    for i in range(column_size):
        line_of_value[i] = data_frame[column_name][i]

    #sort a column and divide it to equal groups for uniform distribution
   # sorted(line_of_value.items(), key=itemgetter(1))
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

def data_preprosessing_equal_range(data_frame, new_data_frame, header_sublist):
    for column in range(len(header_sublist)):
        new_column = []
        max_val = max(data_frame[header_sublist[column]])
        min_val = min(data_frame[header_sublist[column]])
        step_range = (max_val - min_val)/7
        for i in range(len(data_frame[header_sublist[column]])):
            new_column.append(categorize_value_to_equal_range(data_frame[header_sublist[column]][i], min_val, step_range))
        new_data_frame[header_sublist[column]] = new_column
    new_data_frame.to_csv('db_after_preprosessing.csv')

def main():
    data_preprosessing()
    # BayesianModel()


if __name__ == '__main__':
    main()
