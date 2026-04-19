import pandas as pd
from constants import NEEDED_COLUMNS

class DataLoader:
    def __init__(self, path: str) -> None:
        self.path = path 
        self._df = None

    def load(self):
        df = pd.read_csv(self.path, compression="gzip", low_memory=False)
        self._df = df
        return self
    
    def validate(self):
        if self._df is None:
            raise ValueError("сначала вызови load()")
        
        for col in NEEDED_COLUMNS:
            if col not in self._df.columns:
                 raise ValueError(f"колонка {col} не найдена")
        return self 

    def get_data(self)-> pd.DataFrame:
        if self._df is None:
            raise ValueError("через лоад")
        return self._df


