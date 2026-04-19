import pandas as pd
from src.constants import USELESS_COLUMNS, UNIT
class Preprocessor:
    def __init__(self, df : pd.DataFrame) -> None:
        self.df = df

    def del_missing(self):
        self.df = self.df[self.df["OBS_FLAG"] != "m"]
        return self

    def dropping_useless(self):
        self.df = self.df.drop(columns=USELESS_COLUMNS)
        return self
    
    def normalize_to_MIO_T(self):
        self.df = self.df[self.df["unit"] == UNIT]
        return self
    
    def del_na(self):
        self.df = self.df.dropna(subset=["OBS_VALUE"])
        return self
    
    def get_data(self):
        return self.df 
    
    # Preprocessor(df).del_missing().normalize_to_MIO_T().dropping_useless().del_na().get_data()
        