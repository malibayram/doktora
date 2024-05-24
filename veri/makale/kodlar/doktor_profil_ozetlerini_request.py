import requests

tum_doktorlar = []
for i in range(1, 999):
    response = requests.get("https://www.doktorsitesi.com/doktorlar?sayfa=" + str(i))
    doktorlar = htmlden_doktorlari_al(response.text)
    tum_doktorlar.extend(doktorlar)
