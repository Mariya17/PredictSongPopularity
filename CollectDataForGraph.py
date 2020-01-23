import pandas as pd
from collections import OrderedDict
import k2
import BayesianNetwork
import DataPreprocessing
import Measurements
from Const import Files, PreprocessingTypes, GraphType
import PredictSongPopularity
from AdministratorController import AdministratorController
def main():
    administrator = AdministratorController()
    administrator.newFileFlag = True
    administrator.predictor.db_file_name = Files.DB_BEFORE_PREPROCESSING
    administrator.k2InputFileName = Files.K2_INPUT
    # for i in range(3,10):
    #     NUMBER_TO_DIV = i
    administrator.learning()
    administrator.testing()



if __name__ == '__main__':
    main()