from bs4 import BeautifulSoup


def htmlden_doktorlari_al(html):
    soup = BeautifulSoup(html, 'html.parser')
    az_content = soup.find('div', class_='az-content')
    az_main_wrappers = az_content.find_all('div', class_='az-main-wrapper')
    doktorlar = []
    for az_main_wrapper in az_main_wrappers:
        verified = az_main_wrapper.find('div', class_='verified')
        dogrulanmis_profil = False
        if verified is not None:
            dogrulanmis_profil = verified.text
        resim = az_main_wrapper.find('img')
        resim_linki = resim['src']
        cinsiyet = resim['data-gender']
        profil = az_main_wrapper.find('a')
        profil_linki = profil['href']
        konum = profil_linki.split('/')[-1]
        uzmanlik_alani = profil_linki.split('/')[-2]
        unvan = profil.find('span').text
        isim = profil.text.split('\n')[2].strip()
  
        doktorlar.append({
            'resim_linki': resim_linki,
            'unvan': unvan,
            'isim': isim,
            'dogrulanmis_profil': dogrulanmis_profil,
            'profil_linki': profil_linki,
            'cinsiyet': cinsiyet,
            'konum': konum,
            'uzmanlik_alani': uzmanlik_alani
        })
    return doktorlar