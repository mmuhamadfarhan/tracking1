import runpy

runpy.run_path(path_name='bursa_scrapping0K.py')
runpy.run_path(path_name='bursa_scrappingLZ.py')

import os,glob
import pandas as pd

all_files=glob.glob(os.path.join("*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "bursa_scraping.csv")
os.remove("Scrappingbursa0K.csv")
os.remove("ScrappingbursaLZ.csv")



print("Success")