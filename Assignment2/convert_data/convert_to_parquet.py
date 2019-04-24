import pandas as pd
import glob

all_files = glob.glob('*.zip')
# pd.show_versions()

for filename in all_files:
    df = pd.read_csv(filename, compression = 'zip', header = 0, sep = ',', quotechar = '"')
    df.to_parquet('../' + filename + '.parquet.gzip', compression = 'gzip')