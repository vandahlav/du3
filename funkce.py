import json
from json.decoder import JSONDecodeError

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
    except JSONDecodeError:
        print("Načtený vstupní soubor není platný JSON.")
        quit()