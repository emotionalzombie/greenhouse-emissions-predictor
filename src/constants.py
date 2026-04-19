# удаляем
USELESS_COLUMNS = ["DATAFLOW", "LAST UPDATE", "freq", "CONF_STATUS", "OBS_FLAG"]

# нужные колонки 
NEEDED_COLUMNS = ["airpol", "src_crf", "geo", "TIME_PERIOD", "OBS_VALUE", "unit"]

# единица измерения которую оставляем
UNIT = "MIO_T"

# путь к данным
from pathlib import Path
RAW_DATA_PATH = Path(__file__).parent.parent / "data/raw/estat_env_air_gge_en.csv.gz"

# годы датасета
MIN_YEAR = 1990
MAX_YEAR = 2023