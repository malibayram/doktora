import requests
from doktor_profil_ozetlerini_request import htmlden_doktorlari_al


def doktorlari_al():
    tum_doktorlar = []
    for i in range(1, 11):
        url = f'https://www.doktorsitesi.com/doktorlar?sayfa={i}'
        doktorlar = htmlden_doktorlari_al(url)
        tum_doktorlar.extend(doktorlar)
    return tum_doktorlar