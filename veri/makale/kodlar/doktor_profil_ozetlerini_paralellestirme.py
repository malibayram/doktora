import asyncio
import time

import aiohttp
from doktor_profil_ozetlerini_request import htmlden_doktorlari_al

hatali_islemler = []
tum_doktorlar = []

async def doktor_profil_ozetini_getir(session, sayfa_no):
    url = "https://www.doktorsitesi.com/tumuzmanlar?sayfa=" + str(sayfa_no)
    try:
        async with session.get(url) as response:
            html = await response.text()
            doktorlar = htmlden_doktorlari_al(html)
            tum_doktorlar.extend(doktorlar)
    except Exception as e:
        print(f"Error: {e}")
        hatali_islemler.append(sayfa_no)

async def doktorlari_al():
    baslama_zamani = time.time()
    async with aiohttp.ClientSession() as session:
        gorevler = []
        for i in range(1, 9):
            gorevler.append(doktor_profil_ozetini_getir(session, i))
        await asyncio.gather(*gorevler)
    bitis_zamani = time.time()
    print(f"Toplam {len(tum_doktorlar)} doktor profili cekildi. Hatali islem sayisi: {len(hatali_islemler)} Toplam sure: {bitis_zamani - baslama_zamani} saniye")
    
    return tum_doktorlar

