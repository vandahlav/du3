from pyproj import Transformer
import json   
from funkce import prevod_souradnic

#načtení souborů
with open("adresy.geojson", encoding="utf-8") as adresy_2, open("kontejnery.geojson", encoding="utf-8") as kontejnery_2:
    adresy = json.load(adresy_2)
    kontejnery = json.load(kontejnery_2)  

  #načtení a převod adres 
    for feature in adresy ["features"]:
        x_a = feature["geometry"]["coordinates"][0]
        y_a = feature["geometry"]["coordinates"][1]

        #vytvoření nového klíče a uložení do slovníku 
        feature ["geometry"]["coordinates"] = prevod_souradnic(x_a,y_a)
        adresa_ulice = feature ["properties"]["addr:street"]
        adresa_cp = feature ["properties"]["addr:housenumber"]

        #vyselektování jen volných (=veřejných) kontejnerů
        kontejnery_list = []
        for feature in kontejnery["features"]:
            if feature ["properties"]["PRISTUP"] == "volně":
                kontejnery_list.append(feature)
                x_k = feature["geometry"]["coordinates"][0]
                y_k = feature["geometry"]["coordinates"][1]   

    print(x_k,y_k,prevod_souradnic(x_a,y_a))