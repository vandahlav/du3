from pyproj import Transformer
import json   
from funkce import prevod_souradnic
from math import sqrt
from statistics import mean, median

#načtení souborů
with open("adresy.geojson", encoding="utf-8") as adresy_2, open("kontejnery.geojson", encoding="utf-8") as kontejnery_2:
    adresy = json.load(adresy_2)
    kontejnery = json.load(kontejnery_2)  

    #inicializace proměnných 
    nejblizsi_vzdalenost = float('inf')
    pocet_adres = 0
    suma_vzdalenosti = 0
    max_vzdalenost = 10000
    min_vzdalenosti_list = []
    
    #vyselektování jen volných (=veřejných) kontejnerů
    kontejnery_list = []
    for feature in kontejnery["features"]:
        if feature ["properties"]["PRISTUP"] == "volně":
            kontejnery_list.append(feature)    

    #načtení a převod adres 
    for feature in adresy ["features"]:
        x_a = feature["geometry"]["coordinates"][0]
        y_a = feature["geometry"]["coordinates"][1]

        #vytvoření nového klíče a uložení do slovníku 
        feature ["geometry"]["coordinates"] = prevod_souradnic(x_a,y_a)
        x_a,y_a = prevod_souradnic(x_a,y_a)
        adresa_ulice = feature ["properties"]["addr:street"]
        adresa_cp = feature ["properties"]["addr:housenumber"]

        #výpočet nejkratší vzdálenosti z dané adresy ke kontejneru 
        seznam_vzdalenosti = []
        for feature in kontejnery_list:
            x_k, y_k = feature["geometry"]["coordinates"]
            vzdalenost = int(sqrt((x_k - x_a)**2 + (y_k - y_a)**2))
            seznam_vzdalenosti.append(vzdalenost)

        min_vzdalenosti_list.append(min(seznam_vzdalenosti)) 
     
        """if nejblizsi_vzdalenost > max_vzdalenost:
            print(f"Nejbližší vzdálenost ke kontejneru z adresy {adresa_ulice} {adresa_cp} je větší než 10 km. Program končí.")
            adresa_ulice = feature ["properties"]["addr:street"]
            adresa_cp = feature ["properties"]["addr:housenumber"]
            quit()"""

prumerna_vzdalenost = mean(min_vzdalenosti_list)

print(f"Průměrná vzdálenost ke kontejneru je {round(prumerna_vzdalenost)} m.")
print(f"Nejdále to je ke kontejneru z adresy {adresa_ulice} {adresa_cp}.")  #nefunguje



