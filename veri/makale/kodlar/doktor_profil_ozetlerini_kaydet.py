# Doktor profillerini asenkron olarak cekme
import asyncio

from doktor_profil_ozetlerini_paralellestirme import doktorlari_al

tum_doktorlar = asyncio.run(doktorlari_al())

# Doktor profillerini senkron olarak cekme
from doktor_profil_ozetlerini_request import doktorlari_al

tum_doktorlar = doktorlari_al()

import pandas as pd

tum_doktorlar_df = pd.DataFrame(tum_doktorlar)
tum_doktorlar_df.to_csv('tum_doktorlar.csv', index=False)
tum_doktorlar_df.head()