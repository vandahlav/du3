from pyproj import Transformer
import json

def prevod_souradnic(x,y):
    wgs2jtsk = Transformer.from_crs(4326,5514, always_xy=True)
    souradnice = wgs2jtsk.transform(x,y)
    return souradnice

def otevreni_souboru(soubor):
    try:
        with open(soubor, encoding="utf-8") as soubor:
            return json.load(soubor)
    except FileNotFoundError:
        print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
        quit()
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()
