import numpy as np
import pandas as pd

class MyHelper:
  
  def __init__(self):
    pass
  
  def read_csv(self, csv_path):
    try:
        df = pd.read_csv(csv_path)
        print(">> file read as csv")
        return df
    except FileNotFoundError:
        print(">> file not found")
  
  
  def save_csv(self, df, csv_path):
    try:
        df.to_csv(csv_path, index=False)
        print('>> File Successfully Saved.!!!')

    except Exception:
        print(">> Save failed...")

    return df