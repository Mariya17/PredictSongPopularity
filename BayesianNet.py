import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import BayesianEstimator
'''
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

'''
def categorize_value(value, min_val, step_range):
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
def data_preporation():
    data_frame = pd.read_csv('Short_song_data.csv')
   # song_name_column = pd.read_csv('Short_song_data.csv',usecols=['song_name'])
   # song_popularity_column = pd.read_csv('Short_song_data.csv',usecols=['song_popularity'])


    header_list = ["song_name","song_popularity","acousticness","danceability","energy","instrumentalness","key","liveness","loudness","audio_mode","speechiness","tempo","time_signature","audio_valence"]
    header_sublist = ["acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","tempo","audio_valence"]

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


    for column in range(len(header_sublist)):
        new_column = []
        max_val = max(data_frame[header_sublist[column]])
        min_val = min(data_frame[header_sublist[column]])
        step_range = (max_val - min_val)/7
        for i in range(len(data_frame[header_sublist[column]])):
            new_column.append(categorize_value(data_frame[header_sublist[column]][i], min_val, step_range))
        new_data_frame[header_sublist[column]] = new_column
    new_data_frame.to_csv('db_after_preprosessing.csv')

data_preporation()