# DIRECTORY = 'C:/galitProject/PredictSongPopularity/' #Galit
DIRECTORY = '' #Mariya

class Files:
        DB_BEFORE_PREPROCESSING =      DIRECTORY + 'song_data.csv'
        GRAPH =                        DIRECTORY + 'graph.csv'
        K2_INPUT =                     DIRECTORY + 'k2input.csv'
        PREDICT_RESULTS =              DIRECTORY + 'predicted_results.csv'
        PREDICT_RESULTS_SINGLE_SONG =  DIRECTORY + 'predicted_single_song_result.csv'
        DAG =                          DIRECTORY + 'DAG_File.csv'
        DB_AFTER_PREPROCESSING =       DIRECTORY + 'db_after_preprosessing.csv'

class PreprocessingTypes:
        MEAN_SHIFT =            'MeanShirf'     # default
        UNIFORM_DISTRIBUTION =  'Uniform Distribution'
        EQUAL_STEPS =           'Equal Steps'   #UN_UNIFORM
        NUMBER_TO_DIV =         7

class GraphType:
        MSE = 'MSE'
        ERROR_RATE = 'Error Rate'
