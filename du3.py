from pyproj import Transformer
import json   
from funkce import otevreni_souboru
from math import sqrt
from statistics import mean, median

#načtení souborů
adresy = otevreni_souboru("adresy.geojson")
kontejnery = otevreni_souboru("kontejnery.geojson") 

#inicializace proměnných a nastavení konstanty max vzdálenosti 
nejblizsi_vzdalenost = float('inf')
suma_vzdalenosti = 0
nejdelsi_vzdalenost = 0
min_vzdalenosti_list = []
max_vzdalenost = 0
MAX_VZDALENOST = 10000

#převod souřednic
wgs2jtsk = Transformer.from_crs(4326,5514, always_xy=True)

#vyselektování jen volných (=veřejných) kontejnerů
kontejnery_list = []
for feature in kontejnery["features"]:
    if feature ["properties"]["PRISTUP"] == "volně":
        kontejnery_list.append(feature)   

#načtení a převod adres 
for feature in adresy ["features"]:
    try:
        feature["geometry"]["coordinates"] = list(wgs2jtsk.transform(*feature["geometry"]["coordinates"]))
        x_a = feature["geometry"]["coordinates"][0]
        y_a = feature["geometry"]["coordinates"][1]
    except ValueError:
        print(f"Nelze načíst obě souřadnice ze souboru.")
        continue

    #vytvoření nového klíče a uložení do slovníku 
    adresa_ulice = feature ["properties"]["addr:street"]
    adresa_cp = feature ["properties"]["addr:housenumber"]

    #výpočet nejkratší vzdálenosti z dané adresy ke kontejneru 
    try:
        for feature in kontejnery_list:
            x_k, y_k = feature["geometry"]["coordinates"]
            vzdalenost = int(sqrt((x_k - x_a)**2 + (y_k - y_a)**2))

            #seznam_vzdalenosti.append(vzdalenost)
            if vzdalenost < nejblizsi_vzdalenost:
                nejblizsi_vzdalenost = vzdalenost

            kont_vyjimka = feature["properties"]["STATIONNAME"]  
    except ValueError:
        print("Chybně zadaná data u kontejneru na adrese {kont_vyjimka}.")
        continue

    suma_vzdalenosti += nejblizsi_vzdalenost
    min_vzdalenosti_list.append(nejblizsi_vzdalenost)
 
    #zjištění adresy, která to má nejdále ke kontejneru
    if nejblizsi_vzdalenost > nejdelsi_vzdalenost:
        nejdelsi_vzdalenost = nejblizsi_vzdalenost
        adresa_ulice_max = adresa_ulice
        adresa_cp_max = adresa_cp

    #ošetření, aby vzdálenost ke kontejneru nebyla delší, než 10 km
    if nejblizsi_vzdalenost > MAX_VZDALENOST:
        adresa_ulice = feature ["properties"]["addr:street"]
        adresa_cp = feature ["properties"]["addr:housenumber"]
        print(f"Nejbližší vzdálenost ke kontejneru z adresy {adresa_ulice} {adresa_cp} je větší než 10 km. Program končí.")
        quit()
    
    #výpočet mediánu
    m = median(min_vzdalenosti_list)
        
prumerna_vzdalenost = suma_vzdalenosti / len(min_vzdalenosti_list)

print(f"Bylo načteno {len(min_vzdalenosti_list)} adresních bodů.")
print(f"Bylo načteno {len(kontejnery_list)} veřejných kontejnerů na tříděný odpad.\n")
print(f"Průměrná vzdálenost ke kontejneru je {round(prumerna_vzdalenost)} m.")
print(f"Nejdále to je ke kontejneru z adresy {adresa_ulice_max} {adresa_cp_max} a to {nejdelsi_vzdalenost} m.\n")
print(f"Medián vzdáleností ke kontejnerům je {round(m)} m.\n")