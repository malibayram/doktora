import pandas as pd

tum_doktorlar_df = pd.DataFrame(tum_doktorlar)
tum_doktorlar_df.to_csv('tum_doktorlar.csv', index=False)
tum_doktorlar_df.head()