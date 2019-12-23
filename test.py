import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import BayesianEstimator

def BN():
    data = pd.read_csv('db_uniform_distribution.csv')
    model = BayesianModel([('song_duration_ms', 'loudness'), ('tempo', 'loudness'), ('liveness', 'energy'), ('energy', 'song_popularity'), ('loudness', 'song_popularity')])
    #model = BayesianModel([('fruit', 'tasty'), ('size', 'tasty')])  # fruit -> tasty <- size
    pe = ParameterEstimator(model, data)
    print("\n", pe.state_counts('song_duration_ms'))  # unconditional
    print("\n", pe.state_counts('tempo'))  # conditional on fruit and size

    est = BayesianEstimator(model, data)

    print(est.estimate_cpd('tempo', prior_type='BDeu', equivalent_sample_size=10))
    print(est.estimate_cpd('song_popularity', prior_type='BDeu', equivalent_sample_size=10))
