import re
import pandas as pd
from pathlib import Path

def get_artistname_trackname(file:Path):
    df = pd.read_csv(file)
    formated_df = df[["artist_names","track_name"]]
    return formated_df

def _clean(text:str)->str:
    cleaned_string = re.sub(r"\s*\(.*?\)", "", text)
    return cleaned_string
    
if __name__ == "__main__":
    print(_clean("Alibi (with Pabllo Vittar & Yseult) by Sevdaliza, Pabllo Vittar, Yseult"))     