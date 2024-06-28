import config
import pickle
import pandas as pd
  
def load_model():
   with open(config.dt_clf_PATH,'rb') as f:
     return pickle.load(f)
   
def load_data():
   return pd.read_csv(config.DATA_FILE)